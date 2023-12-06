import math
from functools import reduce
times, dists = [list(map(int, line.split()[1:])) for line in open("input.txt", "r").readlines()]
print(reduce(lambda x, y: x * y, [math.floor(time/2.0 + math.sqrt((time/2.0) ** 2 - (dist + 1))) - math.ceil(time/2.0 - math.sqrt((time/2.0) ** 2 - (dist + 1))) + 1 for time, dist in zip(times, dists)]))