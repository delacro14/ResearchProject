import duckdb
import time
import psutil

def get_memory_usage():
    process = psutil.Process()
    memory_info = process.memory_info()
    return memory_info.rss / (1024 * 1024)  # Convert bytes to megabytes

db = duckdb.connect(":memory:")
db.execute("""
INSTALL spatial;
LOAD spatial;
""")

start_memory = get_memory_usage()
start_time = time.time()
start_process_time = time.process_time()
db.execute("""
CREATE TABLE table1 AS SELECT FID, ST_GeomFromWKB(wkb_geometry) AS geom 
FROM ST_Read('./test/simplified_land_polygons.shx');
""")
end_time = time.time()
end_memory = get_memory_usage()
end_process_time = time.process_time()
elapsed_time = end_time - start_time
memory_usage_change = end_memory - start_memory
elapsed_process_time = end_process_time - start_process_time
print(f'Elapsed time {elapsed_time}')
print(f'Memory usage change: {memory_usage_change}')
print(f'Elapsed process time {elapsed_process_time}')
db.sql("""
select count(*) as count from table1
""").show()
db.close()

