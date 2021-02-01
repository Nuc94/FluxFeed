'''
this script is entitled to push files towards influxDB from several .csv files
'''

import pandas as pd
from influxdb import DataFrameClient
from os import listdir
from os.path import join, isfile

SPLIT_CHAR = '_'

DATA_PATH = 'var/lib/data'

protocol = 'line'

client = DataFrameClient(host = 'localhost', port = 8086, database='NOVELTY')

files = [f for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f))]

for filename in files:
    if '.csv' in filename and '_' in filename:
        print(filename)
        df = pd.read_csv(join(DATA_PATH, filename))
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit = 'ms')
        df.set_index('Timestamp', inplace=True)
        filename = filename[:-4] #line to cut away the '.csv' part of the file
        split = filename.split(SPLIT_CHAR)
        dbname = split[0]
        collection = SPLIT_CHAR.join( split[1:] )
        client.create_database(dbname)
        client.switch_database(dbname)
        client.write_points(df, collection, protocol=protocol, batch_size = 100)