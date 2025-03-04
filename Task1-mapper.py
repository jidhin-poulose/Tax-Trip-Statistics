#!/usr/bin/env python3

import sys
from collections import defaultdict

def find_trip_type(distance):
    if distance >= 200:
        return 'long_trips'
    elif distance >= 100:
        return 'medium_trips'
    else:
        return 'short_trips'

# default dictionary:: taxi_id, type =>  [count, max_fare, min_fare, total_fare]        
taxi_details = defaultdict(lambda: {'long_trips': [0, float('-inf'), float('inf'), 0],'medium_trips': [0, float('-inf'), float('inf'), 0],'short_trips': [0, float('-inf'), float('inf'), 0]})


for line in sys.stdin:
    trip, taxi_id, fare, distance, *_ = line.strip().split(',')
    fare = float(fare)
    distance = float(distance)
    
    trip_type = find_trip_type(distance)
    details = taxi_details[taxi_id][trip_type]
    details[0] += 1  # count
    details[1] = max(details[1], fare)  # max_fare
    details[2] = min(details[2], fare)  # min_fare
    details[3] += fare
    
    
for taxi_id, details in taxi_details.items():
    for trip_type, trip_details in details.items():
        if trip_details[0] > 0:  # If count > 0
            count, max_fare, min_fare, total_fare = trip_details
            print('%s\t%s\t%s\t%s\t%s\t%s\t%s' % (hash(taxi_id)%3, taxi_id, trip_type, count, max_fare, min_fare, total_fare))
