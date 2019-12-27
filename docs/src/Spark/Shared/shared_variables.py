lines = sc.textFile("README.md")
l1 = lines.map(lambda line: len(line.split()))
l1.reduce(lambda a,b: a if (a>b) else b)

pairs = lines.flatMap(lambda s: s.split()).map(lambda w: (w,1))
result = pairs.reduceByKey(lambda a,b: a+b)
print("\n".join(map(lambda x: "{} -> {}".format(*x), 
                    result.collect())))

distData = sc.parallelize(list(range(1000))
                          
b = sc.broadcast(list(range(10)))
b.value

a = sc.accumulator(0)
sc.parallelize(list(range(5))).foreach(lambda x: a.add(x))
a.value
