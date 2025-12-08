import math
from itertools import combinations
from collections import defaultdict
boxes = [list(map(int, line.strip().split(','))) for line in open("input.txt", "r").readlines()]
def dist(x, y):
    return math.dist(x, y)
combs = combinations(boxes, 2)
path_distances = sorted(combs, key=lambda pair: dist(pair[0], pair[1]))
point_to_index = {tuple(box): i for i, box in enumerate(boxes)}
index_to_point = {i: tuple(box) for i, box in enumerate(boxes)}
connections = defaultdict(list)
def search(ix, visited):
    if ix in visited:
        return 0
    visited.add(ix)
    size = 1
    for jx in connections[ix]:
        size += search(jx, visited)
    return size
for b1, b2 in path_distances:
    connections[point_to_index[tuple(b1)]].append(point_to_index[tuple(b2)])
    connections[point_to_index[tuple(b2)]].append(point_to_index[tuple(b1)])
    if search(point_to_index[tuple(b1)], set()) == len(boxes):
        print(b1[0]*b2[0])
        exit()
