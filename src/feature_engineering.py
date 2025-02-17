from pyspark.sql import SparkSession
from google.cloud import bigquery

def preprocess_data():
    spark = SparkSession.builder.appName("FeatureEngineering").getOrCreate()
    df = spark.read.format("bigquery").option("table", "your_project.your_dataset.retail_data").load()
    df = df.na.fill(0)
    df.write.format("bigquery").option("table", "your_project.your_dataset.processed_data").mode("overwrite").save()
    print("Feature engineering completed.")