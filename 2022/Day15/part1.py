from collections import defaultdict
import re
from itertools import chain

def manhattan_dist(sensor, beacon):
    x, y = sensor
    xx, yy = beacon
    return abs(x - xx) + abs(y - yy)

input = [list(map(int, re.findall(r'-?\d+', line.strip('\n')))) for line in open("testinput.txt", "r").readlines()]
input = [((lst[0], lst[1]), (lst[2], lst[3])) for lst in input]

blocked_x_ranges = defaultdict(set)
for sensor, beacon in input:
    dist = manhattan_dist(sensor, beacon)
    for dy in range(-dist, dist + 1):
        start, stop = 0, 0
        start = -(abs(abs(dy) - dist))
        stop = abs(abs(dy) - dist) + 1
        if beacon[1] == dy:
            if sensor[0] - beacon[0] < 0:
                start += 1
            else:
                stop -= 1
        blocked_x_ranges[sensor[1] + dy].add(range(start, stop))

print(blocked_x_ranges[10])
print(len(set(chain(*blocked_x_ranges[10]))))
