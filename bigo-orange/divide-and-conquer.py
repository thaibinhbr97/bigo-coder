"""
Divider and conquer

brute force for closest pair of points
O(n^2)

improved method
1. sort by Ox
2. divide into 2 regions left and right -> find the dist_min for each
region
3. in case dist_min belongs to 2 points from each region,
using dist_min to choose 2 points from each region
4. to avoid multiple comparisons, sort by Oy to create a rectangle box.
Find dist from each pair and update dist_min
5. print answer

O(nlogn)
"""

import math

INF = 1e9


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


def distance(p1, p2):
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return (dx * dx + dy * dy) ** 0.5


def bruteForce(points, left, right):
    min_dist = INF
    for i in range(left, right):
        for j in range(i + 1, right):
            min_dist = min(min_dist, distance(points[i], points[j]))
    return min_dist


def stripClosest(point_set, left, right, mid, dist_min):
    point_mid = point_set[mid]
    splitted_points = []
    for i in range(left, right):
        if abs(point_set[i].x - point_mid.x) <= dist_min:
            splitted_points.append(point_set[i])
    splitted_points.sort(key=lambda p: p.y)
    smallest = dist_min
    l = len(splitted_points)
