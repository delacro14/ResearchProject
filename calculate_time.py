import duckdb
import time
import psutil

def get_memory_usage():
    process = psutil.Process()
    memory_info = process.memory_info()
    return memory_info.rss / (1024 * 1024)  # Convert bytes to megabytes

#shapefile_path = '/mnt/c/Users/Barbs/Downloads/Denmark_shapefile/dk_1km.shp'
shapefile_path = '/mnt/c/Users/Barbs/Downloads/land-polygons-split-3857/land_polygons.shp'
#shapefile_path = '/mnt/c/Users/Barbs/Documents/duckdb/taxi_zones.shp'

sql_commands = [
    "INSTALL spatial;",
    "LOAD spatial;",
    f"CREATE TABLE test4 AS SELECT * FROM ST_Read('{shapefile_path}');"
]

start_time = time.time()
start_process_time = time.process_time()
start_memory = get_memory_usage()

with duckdb.connect() as con:
    for sql_command in sql_commands:
        con.execute(sql_command)

end_time = time.time()
end_process_time = time.process_time()
end_memory = get_memory_usage()

time_elapsed = (end_time - start_time) * 1000  # in milliseconds
process_time_elapsed = (end_process_time - start_process_time) * 1000  # in milliseconds
memory_usage_change = end_memory - start_memory

print(f"Wall Time Elapsed: {time_elapsed:.2f} milliseconds")
print(f"CPU Time: {process_time_elapsed:.2f} milliseconds")
print(f"Memory usage: {memory_usage_change:.2f} MB")

