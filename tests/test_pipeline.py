"""
Basic Pipeline Tests for Reddit Finance Spark Project
----------------------------------------------------
These tests validate data loading, schema integrity,
and basic transformations without executing full training.
"""

import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark():
    spark = SparkSession.builder \
        .appName("Reddit_Finance_Test_Pipeline") \
        .master("local[2]") \
        .getOrCreate()
    yield spark
    spark.stop()


def test_dataset_loads(spark):
    """Dataset should load without errors."""
    df = spark.read.option("header", "true").csv("E:/Datasets/00_combined.csv")
    assert df.count() > 0


def test_required_columns_exist(spark):
    """All required columns should be present."""
    df = spark.read.option("header", "true").csv("E:/Datasets/00_combined.csv")
    required_cols = {
        "id", "title", "text", "created_utc", "created_datetime",
        "score", "num_comments", "upvote_ratio",
        "subreddit", "company", "year", "month"
    }
    assert required_cols.issubset(set(df.columns))


def test_basic_filtering_logic(spark):
    """Filtering should reduce empty records."""
    df = spark.read.option("header", "true").csv("E:/Datasets/00_combined.csv")
    filtered = df.dropna(subset=["company", "created_datetime"])
    assert filtered.count() <= df.count()
