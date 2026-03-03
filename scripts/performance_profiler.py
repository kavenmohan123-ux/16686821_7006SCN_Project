"""
Performance Profiler for Spark Pipeline
--------------------------------------
This script is used to profile execution time, caching behavior,
and shuffle performance for key Spark operations.
"""

import time
from pyspark.sql import SparkSession

# Initialize Spark
spark = SparkSession.builder \
    .appName("Reddit_Finance_Performance_Profiler") \
    .config("spark.sql.shuffle.partitions", "200") \
    .getOrCreate()

DATA_PATH = "E:/Datasets/00_combined.csv"

# Load dataset
df = spark.read.option("header", "true").option("inferSchema", "true").csv(DATA_PATH)

print("Initial row count:", df.count())

# -------------------------------
# Profiling: Aggregation
# -------------------------------
start = time.time()
df.groupBy("company").count().collect()
end = time.time()

print(f"Aggregation runtime: {end - start:.2f} seconds")

# -------------------------------
# Profiling: Caching impact
# -------------------------------
df_cached = df.cache()
df_cached.count()

start = time.time()
df_cached.groupBy("company").count().collect()
end = time.time()

print(f"Cached aggregation runtime: {end - start:.2f} seconds")

df_cached.unpersist()

# -------------------------------
# Profiling: Shuffle scaling
# -------------------------------
for partitions in [50, 100, 200, 400]:
    spark.conf.set("spark.sql.shuffle.partitions", partitions)
    start = time.time()
    df.groupBy("company").count().collect()
    end = time.time()
    print(f"Partitions: {partitions}, Runtime: {end - start:.2f} seconds")

spark.stop()
