# Akash Suryawanshi
# 2019CS50416
# And I like programming !

import random
import math

random.seed(1)

my_points = []
n = int(input())
for i in range(n):
    x = random.random()  # random points are generated
    y = random.random()
    my_points.append([x, y])

print(my_points)

X = int(input())
Y = int(input())  # Query point made
my_query_point = [X, Y]


def distance(a, b):  # O(1) time
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def points_with_minimum_distance(points, query_point):
    all_min_points = []
    min_point = points[0]
    min_distance = distance(min_point, query_point)
    for t in range(n):
        k = distance(points[t], query_point)  # O(n) time
        if k < min_distance:
            min_distance = k

    for j in range(n):
        k = distance(points[j], query_point)  # in case there are multiple elements with the same
        if k == min_distance:  # distance from our query point
            all_min_points.append(points[j])  # still the algorithm is O(n)
    return all_min_points


answer = points_with_minimum_distance(my_points, my_query_point)
print(answer)

# closest means minimum distance from our query point.
# Efficient program means good (less) time complexity.
# The program takes O(n) time which is probably the best we could do.

