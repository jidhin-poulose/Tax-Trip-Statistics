#!/usr/bin/env python3

import sys
import string

def main():
    last_taxi_id = None
    cur_copmany = "_"

    for line in sys.stdin:
        line = line.strip()
        try:
            data = line.split("\t")
            if len(data) == 3:
                taxi_id, trip_no, company_id = data[0],data[1],data[2]
            else:
                continue
        except ValueError:
            print([line.split("\t")])            
            continue
        if not last_taxi_id or last_taxi_id != taxi_id:
            last_taxi_id = taxi_id
            cur_copmany = company_id
        elif taxi_id == last_taxi_id and cur_copmany != "_":
            print('%s\t%s' % (cur_copmany, "1"))
            
            
if __name__ == "__main__":
    main()