from collections import defaultdict
import re
from itertools import chain

def manhattan_dist(sensor, beacon):
    x, y = sensor
    xx, yy = beacon
    return abs(x - xx) + abs(y - yy)

input = [list(map(int, re.findall(r'-?\d+', line.strip('\n')))) for line in open("input.txt", "r").readlines()]
input = [((lst[0], lst[1]), (lst[2], lst[3])) for lst in input]
sensors = [lst[0] for lst in input]
beacons = [lst[1] for lst in input]

blocked_x_ranges = defaultdict(set)
for sensor, beacon in zip(sensors, beacons):
    dist = manhattan_dist(sensor, beacon)
    for dy in range(-dist, dist + 1):
        start = -abs(abs(dy) - dist)
        stop = abs(abs(dy) - dist) + 1
        blocked_x_ranges[sensor[1] + dy].add(range(sensor[0] + start, sensor[0] + stop))

col_to_check = 2000000
blocked_pos = set(chain(*blocked_x_ranges[col_to_check]))
beacons_in_blocked_pos = sum([1 for x in blocked_pos if (x, col_to_check) in beacons])
print(len(blocked_pos) - beacons_in_blocked_pos)
