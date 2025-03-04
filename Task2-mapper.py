#!/usr/bin/env python3
import sys
import os

def calc_dist(pt1, pt2):
    return ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)**0.5
    
def get_medoids():
    medoids = []
    with open('initialization.txt', 'r') as f:
        tmp = f.readline().strip()
        # Here even if the v is not given, the code should get the medoids.
        # This implementation is required when the new medoids are writtwn into the initialization.txt
        # because in the file, only the medoids are written into it, not the v value.
        try: 
            v = int(tmp)
        except ValueError:
            v = 0           # dummy value.
            i, j = map(float, tmp.split())
            medoids.append((i, j))
        for line in f:
            i, j = map(float, line.strip().split())
            medoids.append((i, j))
    return medoids, v
    
def map_coord():
    medoids, v = get_medoids()
    k = len(medoids)

    for line in sys.stdin:
        trip = line.strip().split(',')
        if len(trip) == 8:
            try:
                dropoff_x, dropoff_y = float(trip[6]), float(trip[7])
            except valueError:
                continue
            closest_medoid = min(range(k), key=lambda i: calc_dist((dropoff_x, dropoff_y), medoids[i]))
            print(f"{closest_medoid}\t{dropoff_x},{dropoff_y}")
            
if __name__ == "__main__":
    map_coord()