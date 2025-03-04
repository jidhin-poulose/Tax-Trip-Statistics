#!/bin/bash    

set -e

HADOOP_STREAMING_JAR=./hadoop-streaming-3.1.4.jar

TAXI_INPUT=/Input/Taxis.txt
TRIP_INPUT=/Input/Trips.txt
JOIN_OUTPUT=/output/task3_join
COUNT_OUTPUT=/output/task3_count
SORT_OUTPUT=/output/task3_sort

hadoop fs -rm -r -f $JOIN_OUTPUT $COUNT_OUTPUT $SORT_OUTPUT

# Run script for join
hadoop jar $HADOOP_STREAMING_JAR \
-D mapred.reduce.tasks=3 \
-D stream.num.map.output.key.fields=1 \
-file ./Task3-joinMapper.py \
-mapper ./Task3-joinMapper.py \
-file ./Task3-joinReducer.py \
-reducer ./Task3-joinReducer.py \
-input $TAXI_INPUT,$TRIP_INPUT \
-output $JOIN_OUTPUT \


# Run script for count
hadoop jar $HADOOP_STREAMING_JAR \
-D mapred.reduce.tasks=1 \
-file ./Task3-countMapper.py \
-mapper ./Task3-countMapper.py \
-file ./Task3-countReducer.py \
-reducer ./Task3-countReducer.py \
-input $JOIN_OUTPUT \
-output $COUNT_OUTPUT \


# Run script for sort
hadoop jar $HADOOP_STREAMING_JAR \
-D mapred.reduce.tasks=1 \
-file ./Task3-sortMapper.py \
-mapper ./Task3-sortMapper.py \
-file ./Task3-sortReducer.py \
-reducer ./Task3-sortReducer.py \
-input $COUNT_OUTPUT \
-output $SORT_OUTPUT \


echo "Job Run Successfully. Output:"
#hadoop fs -cat $SORT_OUTPUT/part-*
hadoop fs -mkdir -p /Output/Task3/
hadoop fs -cp $SORT_OUTPUT/part-* /Output/Task3/
hadoop fs -cat /Output/Task3/part-*