import sys
from collections import defaultdict, deque
inputs = [r.strip().split(")") for r in open("input.txt", "r").readlines()]
adjacencyList = defaultdict(list)
for parent, child in inputs:
    adjacencyList[parent].append(child)
    adjacencyList[child].append(parent)
target = adjacencyList["SAN"][0]
visited = {"YOU"}
key = adjacencyList["YOU"][0]
frontier = deque([key])
lengths = {key: 0}
while target not in lengths:
    key = frontier.pop()
    length = lengths[key]
    for neighbour in adjacencyList[key]:
        if neighbour not in visited:
            visited.add(neighbour)
            frontier.appendleft(neighbour)
            lengths[neighbour] = length + 1
print(lengths[target])