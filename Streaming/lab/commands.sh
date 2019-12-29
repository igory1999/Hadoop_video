#!/bin/bash

source env.sh

hdfs dfs -mkdir /user/$USER/wordcount
hdfs dfs -rm -r -f /user/$USER/wordcount/output
hdfs dfs -put  /software/matlab-2014b-x86_64/toolbox/distcomp/examples/integration/old/pbs/README /user/$USER/wordcount/

hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar -input /user/$USER/wordcount/README -output /user/$USER/wordcount/streaming-out-py -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py

hdfs dfs -ls /user/$USER/wordcount/streaming-out-py

