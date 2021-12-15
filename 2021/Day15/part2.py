from queue import PriorityQueue
import sys
myin = {(x, y): int(c) for (y, line) in enumerate(open("input.txt", "r").readlines()) for (x, c) in enumerate(line.replace('\n', ''))}
lenX = max([x for (x, y) in myin.keys()]) + 1
lenY = max([y for (x, y) in myin.keys()]) + 1
lenX_extended = lenX * 5
lenY_extended = lenY * 5
target_coord = (lenX_extended - 1, lenY_extended - 1)

def get_distance(neighbour):
    (x, y) = neighbour
    dist = ((x // lenX) + (y // lenY) + myin[x % lenX, y % lenY]) % 9
    return 9 if dist == 0 else dist

def get_neighbours(x, y):
    indices = [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]
    neighbours = []
    for (xx, yy) in indices:
        if xx >= 0 and xx < lenX_extended and yy >= 0 and yy < lenY_extended:
            neighbours.append((xx, yy))
    return neighbours

distances = {(x, y): sys.maxsize for x in range(lenX_extended) for y in range(lenY_extended)}
q = PriorityQueue()
q.put((0, (0, 0)))

while not q.empty():
    prio, (x, y) = q.get()
    if (x, y) == (target_coord):
        break
    for neighbour in get_neighbours(x, y):
        neighbour_dist = prio + get_distance(neighbour)
        if neighbour_dist < distances[neighbour]:
            distances[neighbour] = neighbour_dist
            q.put((neighbour_dist, neighbour))
print(distances[target_coord])
