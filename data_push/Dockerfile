FROM python:3.8

RUN pip3 install pandas

RUN pip3 install influxdb

COPY . .

CMD python3 pusher.py