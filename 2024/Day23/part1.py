from collections import defaultdict
from itertools import combinations
inputs = [line.strip().split('-') for line in open("input.txt", "r").readlines()]
connections = defaultdict(set)
for c1, c2 in inputs:
    connections[c1].add(c2)
    connections[c2].add(c1)
threes = set()
for c1, c2 in [(c1, c2) for c1, c2 in combinations(connections.keys(), 2) if c2 in connections[c1] or c1 in connections[c2]]:
    common = connections[c1] & connections[c2]
    for c3 in common:
        three = ','.join(sorted([c1, c2, c3]))
        threes.add(three)
print(sum([1 for three in threes if any(x[0] == 't' for x in three.split(','))]))