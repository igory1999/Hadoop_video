#!/bin/bash

hdfs dfs -mkdir pig
hdfs dfs -put data/test1.csv pig/
pig -x mapreduce test1.pig

hdfs dfs -put data/mary.txt pig/
hdfs dfs -rm -r cntd.out
pig -x mapreduce test2.pig
hdfs dfs -cat cntd.out/par*


