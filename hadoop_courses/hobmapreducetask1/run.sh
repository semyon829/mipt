#! /usr/bin/env bash

OUT_DIR="streaming_wc_result"

hadoop fs -rm -r -skipTrash ${OUT_DIR}.tmp > /dev/null

yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapreduce.job.name='suhotsky_mapreduce_job1' \
    -D mapreduce.job.reduces=8 \
    -files mapper.py,reducer.py \
    -mapper mapper.py \
    -reducer reducer.py \
    -input /data/wiki/en_articles_part \
    -output ${OUT_DIR}.tmp > /dev/null

hadoop fs -rm -r -skipTrash ${OUT_DIR} > /dev/null

yarn jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -D mapreduce.job.name='suhotsky_mapreduce_job2' \
    -D mapreduce.job.reduces=1 \
    -D stream.num.map.output.key.fields=2 \
    -D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
    -D mapreduce.partition.keycomparator.options='-k2,2nr -k1' \
    -mapper cat \
    -reducer cat \
    -input ${OUT_DIR}.tmp \
    -output ${OUT_DIR} > /dev/null

hdfs dfs -cat ${OUT_DIR}/part-00000 | head -n 10  # Выводим 1-е 10 строк из каждого файла. 
