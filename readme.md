# FluxFeed

This docker-compose launches grafana and influxDB images and lets them run respectively on port 3000 and 8086.

In addition a script is executed in another container to read several csvs from a mounted folder and load them on influx.

## Instruction

To execute the script just run:

```
docker-compose up
```

## Files loading specification

The folder from which data shall be read has to be specified instead of ```./data_test``` in line 18 when defining volumes for data_push service.

In the mounted folder the container will consider .csv files and load them given that they have an underscore _ character inside them to separate dbname from measurement.

The script decides database and measurement destination based on the following convenction:

```
DATABASE_MEASUREMENT.csv
```

in which the first part of the filename expresses the database name while the second one represent the measurement name.

Every .csv file is required to have a "Timestamp" column, expressing for every row the measurement's timestamp express in milliseconds.