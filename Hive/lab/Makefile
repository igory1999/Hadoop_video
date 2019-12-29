generate: 
	./generate_commands.sh
data:
	hdfs dfs -mkdir pig | true
	hdfs dfs -put data/test1.csv hive/
batch: 
	hive -f commands.sql > out.txt 2> err.txt
sql:
	hive --database ${USER} -e 'select * from t1;'
clean:
	rm -f commands commands.sql *.txt *~ *.log *.csv
