from pyspark.sql import SparkSession

def preprocess_data():
    spark = SparkSession.builder.appName("FeatureEngineering").getOrCreate()
    df = spark.read.format("bigquery").option("table", "charismatic-age-451204-v4.retail_dataset.retail_data").load()
    df = df.na.fill(0)
    df.write.format("bigquery").option("table", "charismatic-age-451204-v4.retail_dataset.processed_data").mode("overwrite").save()
    print("Feature engineering completed.")

if __name__ == "__main__":
    preprocess_data()
