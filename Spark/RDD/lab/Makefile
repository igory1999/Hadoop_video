rdd:
	spark-submit --master local[3] --name 'Line counting with RDD' line_count_RDD.py README.md 1>rdd.out 2>rdd.err
clean:
	rm -r -f *~ *.out *.err spark-warehouse
