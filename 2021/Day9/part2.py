import heapq
from functools import reduce
myin = {(x, y): int(c) for (y, line) in enumerate(open("input.txt", "r").readlines()) for (x, c) in enumerate(line.replace('\n', ''))}
maxX = max([x for (x, y) in myin.keys()])
maxY = max([y for (x, y) in myin.keys()])
def get_neighbours(x, y):
    indices = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    neighbours = []
    for (xx, yy) in indices:
        if xx >= 0 and xx <= maxX and yy >= 0 and yy <= maxY:
            if myin[(xx, yy)] != 9:
                neighbours.append((xx, yy))
    return neighbours
def get_neighbour_values(x, y):
    return [myin[(x, y)] for (x, y) in get_neighbours(x, y)]
low_points = []
for ((x, y), height) in myin.items():
    if height == 9:
        continue
    neighbour_values = get_neighbour_values(x, y)
    if height < min(neighbour_values):
        low_points.append((x, y))
basin_sizes = []
for point in low_points:
    q = [point]
    visited = [point]
    while q:
        (x, y) = q.pop()
        neighbours = get_neighbours(x, y)
        for neighbour in neighbours:
            if neighbour not in visited:
                visited.append(neighbour)
                q.append(neighbour)
    basin_sizes.append(len(visited))
print(reduce(lambda x, y: x * y, heapq.nlargest(3, basin_sizes)))
