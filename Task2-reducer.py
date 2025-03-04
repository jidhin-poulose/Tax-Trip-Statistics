#!/usr/bin/env python3
import sys

def calc_dist(pt1, pt2):
    return ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)**0.5
    
def get_medoids():
    medoids = []
    with open('initialization.txt', 'r') as f:
        tmp = f.readline().strip()
        try: 
            v = int(tmp)
        except ValueError:
            v = 0
            i, j = map(float, tmp.split())
            medoids.append((i, j))
        for line in f:
            i, j = map(float, line.strip().split())
            medoids.append((i, j))
    return medoids, v

# Method for finding the best medoid in each cluster. Based on the minimum cost, 
# the best medoid is selected as the final medoid and printed in the output file directly.   
def get_best_medoid(medoid, points, current_medoid):
    best_medoid = current_medoid
    min_cost = float('inf')

    for tmp_med in points:
        cost = sum(calc_dist(tmp_med, point) for point in points)
        if cost < min_cost:
            min_cost = cost
            best_medoid = tmp_med

    print(f"{best_medoid[0]}\t{best_medoid[1]}")

def reduce():
    medoids, v = get_medoids()
    current_medoid = None
    points = []

    for line in sys.stdin:
        medoid, point = line.strip().split('\t')
        medoid = int(medoid)
        x, y = map(float, point.split(','))

        if current_medoid is None:
            current_medoid = medoid

        if medoid != current_medoid:
            get_best_medoid(current_medoid, points, medoids[current_medoid])
            current_medoid = medoid
            points = []

        points.append((x, y))

    if points:
        get_best_medoid(current_medoid, points, medoids[current_medoid])

if __name__ == "__main__":
    reduce()
