from pyspark.sql import SparkSession

spark = SparkSession \
        .builder \
        .appName("Python Spark SQL basic example") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()

js = "data/people.json"
df = spark.read.json(js)
df.show()
print("="*30)
df.printSchema()
print("="*30)
df.select("name").show()
print("="*30)
df.select(df['name'], df['age'] + 1).show()
print("="*30)
df.filter(df['age'] > 21).show()
print("="*30)
df.groupBy("age").count().show()
print("="*30)

# Register the DataFrame as a SQL temporary view
df.createOrReplaceTempView("people")
sqlDF = spark.sql("SELECT * FROM people")
sqlDF.show()


