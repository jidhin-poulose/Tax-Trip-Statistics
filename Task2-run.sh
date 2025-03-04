#!/bin/bash    

INPUT_PATH=/Input/Trips.txt
OUTPUT_BASE_PATH=/output/kmedoid

NUM_ITER=$(head -n 1 initialization.txt | tr -d '[:space:]')

echo "Retrieved number of iterations: '$NUM_ITER'"

for ((i=0; i < NUM_ITER; i++))
do
    echo "Running iteration $i"
    
    OUTPUT_PATH=${OUTPUT_BASE_PATH}_$i
    
    hadoop jar ./hadoop-streaming-3.1.4.jar \
        -D mapred.reduce.tasks=3 \
        -file ./initialization.txt \
        -file ./Task2-mapper.py \
        -mapper ./Task2-mapper.py \
        -file ./Task2-reducer.py \
        -reducer ./Task2-reducer.py \
        -input $INPUT_PATH \
        -output $OUTPUT_PATH 

    # Update the new medoids
    hadoop fs -cat ${OUTPUT_PATH}/part-* > temp_initial.txt
    
    # Sort the temporary file and the initialization file
    sort temp_initial.txt > sorted_temp_initial.txt
    sort initialization.txt > sorted_initialization.txt
    
    # Compare the sorted files
    diff sorted_temp_initial.txt sorted_initialization.txt > x
    
    # Check the size of the diff output file
    size=$(ls -l x | awk '{print $5}') # Get the size of the file x
    
    if [ "$size" -eq 0 ]; then # If size is 0, no differences
        echo "The medoids converged at the iternation number $i" 		#
        hadoop fs -cat ${OUTPUT_PATH}/part-* > initialization.txt
        break
    else
        # There are differences, update the initialization file
        hadoop fs -cat ${OUTPUT_PATH}/part-* > initialization.txt
    fi

done

hadoop fs -cat ${OUTPUT_BASE_PATH}_$i/part-*


# Clean up and prepare final output
hadoop fs -mkdir -p /Output/Task2/
hadoop fs -cp ${OUTPUT_BASE_PATH}_$i/part-* /Output/Task2/

# Print the final medoids
echo "Final medoids:"
hadoop fs -cat /Output/Task2/part-*

# each time a job is done with Task2-run.sh, a new initialization.txt needs to saved in the master 
# node as the old will be written with the output of the last job run.