from functools import lru_cache
from math import prod
from collections import defaultdict
input = defaultdict(set)
for line in open("input.txt", "r").readlines():
    input[line.split(':')[0]].update(line.split(':')[1].strip().split())
@lru_cache(None)
def DFS(start, end):
    if end == start:
        return 0
    if end in input[start]:
        return 1
    else:
        return sum([DFS(neighbour, end) for neighbour in input[start]])
print(prod([DFS('svr', 'fft'), DFS('fft', 'dac'), DFS('dac', 'out')]) + prod([DFS('svr', 'dac'), DFS('dac', 'fft'), DFS('fft', 'out')]))
