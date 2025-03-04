#!/usr/bin/env python3
import sys

current_key = None
current_details = None

for line in sys.stdin:
    data = line.strip()
    tr_no, taxi_id, tr_type, count, max_fare, min_fare, total_fare = data.split('\t')
    try:
        count = int(count)
        max_fare = float(max_fare)
        min_fare = float(min_fare)
        total_fare = float(total_fare)
    except ValueError:
        continue   
    
    if current_key == (taxi_id, tr_type):
        current_details[0] += count
        current_details[1] = max(current_details[1], max_fare)
        current_details[2] = min(current_details[2], min_fare)
        current_details[3] = current_details[3] + total_fare
    else:
        if current_key:
            avg_fare = current_details[3]/current_details[0]    # grand total / total count
            print('%s\t%s\t%s\t%s\t%s\t%s' % (current_key[0], current_key[1], current_details[0], current_details[1], current_details[2], avg_fare))
        current_key = (taxi_id, tr_type)
        current_details = [count, max_fare, min_fare, total_fare]

if current_key:
    avg_fare = current_details[3]/current_details[0]    # grand total / total count
    print('%s\t%s\t%s\t%s\t%s\t%s' % (current_key[0], current_key[1], current_details[0], current_details[1], current_details[2], avg_fare))