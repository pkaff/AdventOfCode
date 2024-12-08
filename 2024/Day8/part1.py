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
antinodes = set()
for antenna, points in antennas.items():
    for p1, p2 in combinations(points, 2):
        new_point1 = (2*p1[0] - p2[0], 2*p1[1] - p2[1])
        if inside_bounds(new_point1):
            antinodes.add(new_point1)
        new_point2 = (2*p2[0] - p1[0], 2*p2[1] - p1[1])
        if inside_bounds(new_point2):
            antinodes.add(new_point2)
print(len(antinodes))