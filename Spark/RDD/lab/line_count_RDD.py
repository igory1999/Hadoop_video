from pyspark import SparkContext, SparkConf
import sys

try:
    inputFile = sys.argv[1]
except:
    print("Usage: spark-submit --master local[4] --name 'Line counting example' line_count.py <text file> 1>out 2>err")
    sys.exit(1)


# conf = SparkConf().setAppName(appName).setMaster(master)

conf = SparkConf()
sc = SparkContext(conf=conf)

print(sc)
inputData = sc.textFile(inputFile).cache()
print(type(inputData))

numAs = inputData.filter(lambda s: 'a' in s).count()
numBs = inputData.filter(lambda s: 'b' in s).count()

print("Lines with a: %i, lines with b: %i" % (numAs, numBs))

