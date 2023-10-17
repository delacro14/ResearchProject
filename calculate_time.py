import duckdb
import time

#shapefile_path = '/mnt/c/Users/Barbs/Downloads/Denmark_shapefile/dk_1km.shp'
shapefile_path = '/mnt/c/Users/Barbs/Documents/duckdb/taxi_zones.shp'

sql_commands = [
    "INSTALL spatial;",
    "LOAD spatial;",
    f"CREATE TABLE test3 AS SELECT * FROM ST_Read('{shapefile_path}');"
]

start_time = time.time()
start_process_time = time.process_time()

with duckdb.connect() as con:
    for sql_command in sql_commands:
        con.execute(sql_command)

end_time = time.time()
end_process_time = time.process_time()
time_elapsed = (end_time - start_time) * 1000  # in milliseconds
process_time_elapsed = (end_process_time - start_process_time) * 1000  # in milliseconds

print(f"Wall Time Elapsed: {time_elapsed:.2f} milliseconds")
print(f"CPU Time: {process_time_elapsed:.2f} milliseconds")
