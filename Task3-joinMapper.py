#!/usr/bin/env python3
import sys
import os

def main():
    #filename = os.environ['mapreduce_map_input_file']

    for line in sys.stdin:
        taxi_id = ""
        trip_no = "0000"
        company_id = "_"
        
        line = line.strip()
        data = line.split(",")
        if len(data) == 8:
            taxi_id = data[1]
            if len(taxi_id) == 1:
                taxi_id = (f"0{taxi_id}")
            trip_no = data[0]
        elif len(data) == 4:
            taxi_id = data[0]
            if len(taxi_id) == 1:
                taxi_id = (f"0{taxi_id}")
            company_id = data[1]
        print('%s\t%s\t%s' % (taxi_id, trip_no, company_id))
        
if __name__ == "__main__":
    main()