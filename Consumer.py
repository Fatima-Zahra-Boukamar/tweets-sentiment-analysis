import os
os.environ["HADOOP_HOME"] = "C:\\winutils"
os.environ['PATH'] = f"{os.environ['HADOOP_HOME']}/bin;{os.environ['PATH']}"
os.environ["PYSPARK_PYTHON"] = "C:\\Users\\pc\\anaconda3\\python.exe"

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType

schema = StructType() \
    .add("text", StringType()) \
    .add("sentiment", StringType())

spark = SparkSession.builder \
    .appName("KafkaToMongo") \
    .master("local[*]") \
    .config("spark.hadoop.mapreduce.fileoutputcommitter.algorithm.version", "2") \
    .config("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.LocalFileSystem") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.5,org.mongodb.spark:mongo-spark-connector_2.12:10.3.0") \
    .config("spark.hadoop.io.native.lib.available", "false") \
    .getOrCreate()

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "tweets") \
    .load()

tweets_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

query = tweets_df.writeStream \
    .format("mongodb") \
    .outputMode("append") \
    .option("uri", "mongodb://localhost:27017") \
    .option("database", "tweets_db") \
    .option("collection", "tweets") \
    .option("checkpointLocation", "C:\\temp\\checkpoint") \
    .start()

#query = tweets_df.writeStream \
 #   .format("console") \
  #  .outputMode("append") \
   # .option("checkpointLocation", "C:\\temp\\checkpoint") \
    #.start()
#query.awaitTermination()