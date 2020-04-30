from collections import defaultdict
import re

input = [list(map(int, re.findall(r'-?\d+', l))) for l in open("input.txt", "r").readlines()]
strongBot = max(input, key = lambda i: i[3])
def manhattanDist(b1, b2):
    return abs(b1[0] - b2[0]) + abs(b1[1] - b2[1]) + abs(b1[2] - b2[2])

print(sum(1 for i in input if manhattanDist(i, strongBot) <= strongBot[3]))