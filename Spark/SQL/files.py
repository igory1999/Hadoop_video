from pyspark.sql import SparkSession
from os.path import abspath

warehouse_location = abspath('spark-warehouse')

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL Hive integration example") \
    .config("spark.sql.warehouse.dir", warehouse_location) \
    .enableHiveSupport() \
    .getOrCreate()

df = spark.read.load("data/users.parquet")
df.select("name", "favorite_color").write.save("output/namesAndFavColors.parquet")

df = spark.sql("SELECT * FROM parquet.`data/users.parquet`")
print(df.show())

try:
    df.write.saveAsTable("users1") #by default goes to ./spark_warehouse
except:
    pass

try:
    df.write.option("path", "output/hive").saveAsTable("users")
except:
    pass
