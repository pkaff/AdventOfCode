from queue import PriorityQueue
import sys
myin = {(x, y): int(c) for (y, line) in enumerate(open("input.txt", "r").readlines()) for (x, c) in enumerate(line.replace('\n', ''))}
maxX = max([x for (x, y) in myin.keys()])
maxY = max([y for (x, y) in myin.keys()])
distances = {(x, y): sys.maxsize for x in range(maxY + 1) for y in range(maxX + 1)}
q = PriorityQueue()
q.put((0, (0, 0)))

def get_neighbours(x, y):
    indices = [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]
    neighbours = []
    for (xx, yy) in indices:
        if xx >= 0 and xx <= maxX and yy >= 0 and yy <= maxY:
            neighbours.append((xx, yy))
    return neighbours

while not q.empty():
    prio, (x, y) = q.get()
    if (x, y) == (maxX, maxY):
        break
    for neighbour in get_neighbours(x, y):
        neighbour_dist = prio + myin[neighbour]
        if neighbour_dist < distances[neighbour]:
            distances[neighbour] = neighbour_dist
            q.put((neighbour_dist, neighbour))
print(distances[maxX, maxY])
