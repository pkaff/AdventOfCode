import re

def manhattan_dist(sensor, beacon):
    x, y = sensor
    xx, yy = beacon
    return abs(x - xx) + abs(y - yy)

class Sensor:
    def __init__(self, sensor, beacon):
        self.center = sensor
        dist = manhattan_dist(sensor, beacon)
        self.max_dist = dist
    def get_row_range(self, row):
        if row > self.center[1] + self.max_dist or row < self.center[1] - self.max_dist:
            return None

        dist_from_center = abs(self.center[1] - row)
        start = -(self.max_dist - dist_from_center)
        stop = self.max_dist - dist_from_center
        return range(self.center[0] + start, self.center[0] + stop + 1)

def merge(sensor_ranges):
    merged = [sensor_ranges[0]]
    for current in sensor_ranges:
        previous = merged[-1]
        if current.start <= previous.stop:
            merged[-1] = range(min(current.start, previous.start), max(current.stop, previous.stop))
        else:
            merged.append(current)
    return merged

input = [list(map(int, re.findall(r'-?\d+', line.strip('\n')))) for line in open("input.txt", "r").readlines()]
input = [((lst[0], lst[1]), (lst[2], lst[3])) for lst in input]
sensor_points = [lst[0] for lst in input]
beacons = [lst[1] for lst in input]

sensors = []
for sensor, beacon in zip(sensor_points, beacons):
    sensors.append(Sensor(sensor, beacon))

row = 2000000
sensor_ranges = []
for sensor in sensors:
    row_range = sensor.get_row_range(row)
    if row_range:
        sensor_ranges.append(row_range)
sensor_ranges.sort(key=lambda r: r.start)
sensor_ranges = merge(sensor_ranges)
print(sum(1 for _ in sensor_ranges[0]) - sum(1 for beacon in set(beacons) if beacon[1] == row))
