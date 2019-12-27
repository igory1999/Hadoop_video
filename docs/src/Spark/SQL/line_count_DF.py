from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession
import sys

try:
    inputFile = sys.argv[1]
except:
    print("Usage: spark-submit --master local[4] line_count.py <text file> 1>out 2>err")
    sys.exit(1)
    
#spark = SparkSession.builder().appName(appName).master(master).getOrCreate()

conf = SparkConf()
print(conf)
sc = SparkContext(conf=conf)
print(sc)
spark = SparkSession(sc)

print(spark)
inputData = spark.read.text(inputFile).cache()
print(type(inputData))

numAs = inputData.filter(inputData.value.contains('a')).count()
numBs = inputData.filter(inputData.value.contains('b')).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

spark.stop()
