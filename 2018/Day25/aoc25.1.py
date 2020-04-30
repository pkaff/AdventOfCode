import re
from collections import defaultdict

input = [tuple(map(int, l.split(','))) for l in open("input.txt", "r").readlines()]
constellations = []
def manhattanDist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2]) + abs(p1[3] - p2[3])
def findConstellation(constellations, point):
    ixs = []
    for ix, c in enumerate(constellations):
        for p in c:
            if manhattanDist(p, point) <= 3:
                ixs.append(ix)
                break
    return ixs
def merge(constellations, ix, p):
    startIx = ix[0]
    constellations[startIx].append(p)
    for cIx in reversed(ix[1:]):
        constellations[startIx].extend(constellations.pop(cIx))
    
for i in input:
    ix = findConstellation(constellations, i)
    if len(ix) == 0:
        constellations.append([i])
    elif len(ix) == 1:
        constellations[ix[0]].append(i)
    else:
        merge(constellations, ix, i)
print(len(constellations))