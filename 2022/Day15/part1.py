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

class Intervals:
    def __init__(self):
        self.ranges = []
        self.ix = 0
    def merge(self):
        for ix, (r1, r2) in enumerate(zip(self.ranges[1:], self.ranges[:-1])):
            if max(r1.start, r2.start) <= min(r1.stop, r2.stop):
                self.ranges[ix] = range(min(r1.start, r2.start), max(r1.stop, r2.stop))
                del self.ranges[ix + 1]
                return True
        return False
    def append(self, r):
        self.ranges.append(r)
        self.ranges.sort(key=lambda r: r.start)

        while self.merge():
            pass
    def count(self, beacons):
        count = 0
        for r in self.ranges:
            count += r.stop - r.start
            count -= sum([1 for pos in beacons if pos in r])
        return count
    def __str__(self):
        return str(self.ranges)
    def __repr__(self):
        return str(self)

row_to_check = 2000000

blocked_x_ranges = defaultdict(Intervals)
for sensor, beacon in zip(sensors, beacons):
    dist = manhattan_dist(sensor, beacon)
    for dy in range(-dist, dist + 1):
        if sensor[1] + dy == row_to_check:
            start = -abs(abs(dy) - dist)
            stop = abs(abs(dy) - dist) + 1
            blocked_x_ranges[sensor[1] + dy].append(range(sensor[0] + start, sensor[0] + stop))

beacons_in_row = [beacon[0] for beacon in set(beacons) if beacon[1] == row_to_check]
print(blocked_x_ranges[row_to_check].count(beacons_in_row))
