from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, FloatType

# Initialize Spark
spark = SparkSession.builder.appName("Simple PySpark Demo").getOrCreate()

# Define schema
schema = StructType([
    StructField("name", StringType(), False),
    StructField("age", IntegerType(), True),
    StructField("salary", FloatType(), True)
])

# Read sample CSV
print("Reading data...")
df = spark.read.schema(schema).option("header", "true").csv("sample_data.csv")

print("Show data:")
df.show()
