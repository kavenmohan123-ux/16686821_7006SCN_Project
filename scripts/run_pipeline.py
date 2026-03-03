"""
Run Distributed Reddit Finance Pipeline
--------------------------------------
This script initializes Spark, loads the dataset,
runs preprocessing, model training, and evaluation.
"""

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import LogisticRegression, RandomForestClassifier, GBTClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Initialize Spark
spark = SparkSession.builder \
    .appName("Reddit_Finance_EndToEnd_Pipeline") \
    .config("spark.sql.shuffle.partitions", "200") \
    .getOrCreate()

# Load dataset
DATA_PATH = "E:/Datasets/00_combined.csv"
df = spark.read.option("header", "true").option("inferSchema", "true").csv(DATA_PATH)

# Basic cleaning
df = df.dropna(subset=["company", "created_datetime"])

# Label definition
df = df.withColumn(
    "label",
    F.when((F.col("score") > 10) & (F.col("num_comments") > 5), 1).otherwise(0)
)

# Feature assembly
assembler = VectorAssembler(
    inputCols=["score", "num_comments", "upvote_ratio"],
    outputCol="features"
)

df_ml = assembler.transform(df).select("features", "label")

train_df, test_df = df_ml.randomSplit([0.8, 0.2], seed=42)

# Models
lr = LogisticRegression(maxIter=20)
rf = RandomForestClassifier(numTrees=50, maxDepth=8)
gbt = GBTClassifier(maxIter=20, maxDepth=5)

lr_model = lr.fit(train_df)
rf_model = rf.fit(train_df)
gbt_model = gbt.fit(train_df)

# Evaluation
evaluator = BinaryClassificationEvaluator(metricName="areaUnderROC")

print("LR AUC:", evaluator.evaluate(lr_model.transform(test_df)))
print("RF AUC:", evaluator.evaluate(rf_model.transform(test_df)))
print("GBT AUC:", evaluator.evaluate(gbt_model.transform(test_df)))

spark.stop()
