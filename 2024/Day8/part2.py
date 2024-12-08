from itertools import combinations
from collections import defaultdict
input = open("input.txt", "r").readlines()
width = len(input[0].strip())
height = len(input)
antennas = defaultdict(list)
for y, line in enumerate(input):
    for x, node in enumerate(line.strip()):
        if node != '.':
            antennas[node].append((x, y))
def inside_bounds(p):
    return p[0] >= 0 and p[0] < width and p[1] >= 0 and p[1] < height
def next_point(p1, p2):
    return (2*p1[0] - p2[0], 2*p1[1] - p2[1])
antinodes = set()
for antenna, points in antennas.items():
    for p1, p2 in combinations(points, 2):
        antinodes.add(p1)
        antinodes.add(p2)
        new_point = next_point(p1, p2)
        prev_point = p1
        while inside_bounds(new_point):
            antinodes.add(new_point)
            tmp = next_point(new_point, prev_point)
            prev_point = new_point
            new_point = tmp
        new_point = next_point(p2, p1)
        prev_point = p2
        while inside_bounds(new_point):
            antinodes.add(new_point)
            tmp = next_point(new_point, prev_point)
            prev_point = new_point
            new_point = tmp
print(len(antinodes))