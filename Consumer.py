from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType

# Schema to match producer's data
schema = StructType() \
    .add("text", StringType()) \
    .add("sentiment", DoubleType())

# Initialize Spark session
#spark = SparkSession.builder \
 #   .appName("KafkaToMongo") \
  #  .master("local[*]") \
   # .config("spark.mongodb.output.uri", "mongodb://admin:admin123@mongodb:27017/tweets_db.tweets?authSource=admin") \
    #.config("spark.jars", "/opt/bitnami/spark/jars/spark-sql-kafka-0-10_2.12-3.5.0.jar,/opt/bitnami/spark/jars/kafka-clients-3.4.1.jar,/opt/bitnami/spark/jars/spark-token-provider-kafka-0-10_2.12-3.5.0.jar,/opt/bitnami/spark/jars/commons-pool2-2.11.1.jar,/opt/bitnami/spark/jars/mongo-spark-connector_2.12-10.3.0.jar,/opt/bitnami/spark/jars/mongodb-driver-sync-5.1.1.jar,/opt/bitnami/spark/jars/mongodb-driver-core-5.1.1.jar,/opt/bitnami/spark/jars/bson-5.1.1.jar") \
    #.getOrCreate()
spark = SparkSession.builder \
    .appName("KafkaToMongo") \
    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:10.3.0,org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0") \
    .config("spark.mongodb.connection.uri", "mongodb://admin:admin123@mongodb:27017") \
    .config("spark.mongodb.database", "tweets_db") \
    .config("spark.mongodb.collection", "tweets") \
    .getOrCreate()

# Read from Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "kafka:29092") \
    .option("subscribe", "tweets") \
    .load()

# Parse JSON data
tweets_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Write to MongoDB
query = tweets_df.writeStream \
    .format("mongodb") \
    .option("checkpointLocation", "/app/checkpoint") \
    .outputMode("append") \
    .start()


query.awaitTermination()