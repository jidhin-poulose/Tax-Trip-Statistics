

################################################################
# Remove all Output dirs on HDFS
hadoop fs -rm -r /Output
# unzip zip file 
# Copying the streaming jar to the current working dir
scp -i s4023503-cosc2637.pem ./hadoop-streaming-3.1.4.jar hadoop@s4023503.emr.cosc2637.route53.aws.rmit.edu.au:~/
# Copying the "initialization.txt" (for task2) to the current working dir. 
# Each time a job is done with Task2-run.sh, a new initialization.txt needs to saved in the master 
# node as the old will be written with the output of the last job run.
scp -i s4023503-cosc2637.pem ./initialization.txt hadoop@s4023503.emr.cosc2637.route53.aws.rmit.edu.au:~/
Copy all the code files to the current working dir
scp -i s4023503-cosc2637.pem ./s4023503_BDP_A1/* hadoop@s4023503.emr.cosc2637.route53.aws.rmit.edu.au:~/


scp -i s4023503-cosc2637.pem ./Trips.txt hadoop@s4023503.emr.cosc2637.route53.aws.rmit.edu.au:~/
scp -i s4023503-cosc2637.pem ./Taxis.txt hadoop@s4023503.emr.cosc2637.route53.aws.rmit.edu.au:~/






# Copying the input files to HDFS root dir from my current working dir
hadoop fs -mkdir /Input
hadoop fs -put Trips.txt /Input/
hadoop fs -put Taxis.txt /Input/
hadoop fs -ls /Input


# install dos2unix
sudo yum install dos2unix
dos2unix Task*
chmod +x Task*
################################################################
# Run task 1
./Task1-run.sh
# copy the task 1 output to the current dir
hadoop fs -getmerge /Output/Task1/part* Task1_output.txt
cat Task1_output.txt

################################################################
# Run task 2
./Task2-run.sh
# copy the task 2 output to the current dir
hadoop fs -getmerge /Output/Task2/part* Task2_output.txt 

################################################################
# Run task 3
./Task3-run.sh
# copy the task 3 output to the current dir
hadoop fs -getmerge /Output/Task3/part* Task3_output.txt 
cat Task3_output.txt
