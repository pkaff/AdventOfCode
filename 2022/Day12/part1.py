from queue import PriorityQueue
import sys

graph = dict()
start = tuple()
stop = tuple()
for (y, line) in enumerate(open("input.txt", "r").readlines()):
    for (x, c) in enumerate(line.replace('\n', '')):
        if c == 'S':
            graph[(x, y)] = 0
            start = (x, y)
        elif c == 'E':
            graph[(x, y)] = 25
            stop = (x, y)
        else:
            graph[(x, y)] = ord(c) - 97

maxX = max([x for (x, y) in graph.keys()])
maxY = max([y for (x, y) in graph.keys()])
distances = {(x, y): sys.maxsize for x in range(maxX + 1) for y in range(maxY + 1)}

def get_neighbours(x, y):
    indices = [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]
    neighbours = []
    for (xx, yy) in indices:
        if xx >= 0 and xx <= maxX and yy >= 0 and yy <= maxY:
            neighbours.append((xx, yy))
    return neighbours

q = PriorityQueue()
q.put((0, start))

while not q.empty():
    dist, (x, y) = q.get()
    if (x, y) == stop:
        continue
    for neighbour in get_neighbours(x, y):
        neighbour_dist = dist + 1
        if graph[neighbour] <= graph[(x, y)] + 1 and neighbour_dist < distances[neighbour]:
            distances[neighbour] = neighbour_dist
            q.put((neighbour_dist, neighbour))
print(distances[stop])