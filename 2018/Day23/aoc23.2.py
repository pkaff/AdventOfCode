from collections import defaultdict
import re

input = [list(map(int, re.findall(r'-?\d+', l))) for l in open("input.txt", "r").readlines()]
def manhattanDist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])
def distToOrigin(coord):
    return manhattanDist(coord, (0, 0, 0))
xs = [p[0] for p in input]
ys = [p[1] for p in input]
zs = [p[2] for p in input]
dist = 1
while 2*dist < max(xs) - min(xs):# or dist < max(ys) - min(ys) or dist < max(zs) - min(zs):
    dist *= 2
while True:
    maxNInRange = 0
    bestPoint = (min(xs), min(ys), min(zs))
    for x in range(min(xs), max(xs) + 1, dist):
        for y in range(min(ys), max(ys) + 1, dist):
            for z in range(min(zs), max(zs) + 1, dist):
                nInRange = 0
                for point in input:
                    if manhattanDist(point, (x, y, z)) <= point[3]:
                        nInRange += 1
                if nInRange > maxNInRange or (nInRange == maxNInRange and distToOrigin((x, y, z)) < distToOrigin(bestPoint)):
                    maxNInRange = nInRange
                    bestPoint = (x, y, z)
                     
    if dist == 1:
        print(distToOrigin(bestPoint))
        break
    else:
        xs = [bestPoint[0] - dist, bestPoint[0] + dist]
        ys = [bestPoint[1] - dist, bestPoint[1] + dist]
        zs = [bestPoint[2] - dist, bestPoint[2] + dist]
        dist //= 2