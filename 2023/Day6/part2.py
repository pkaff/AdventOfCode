import math
time, dist = [int(''.join(line.split()[1:])) for line in open("input.txt", "r").readlines()]
print(math.floor(time/2.0 + math.sqrt((time/2.0) ** 2 - (dist + 1))) - math.ceil(time/2.0 - math.sqrt((time/2.0) ** 2 - (dist + 1))) + 1)