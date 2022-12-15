from collections import defaultdict

input = [line.strip('\n').split(' -> ') for line in open("input.txt", "r").readlines()]
walls = defaultdict(lambda: False)

maxY = 0

for connections in input:
    for point_from, point_to in zip(connections[:-1], connections[1:]):
        fromx, fromy = list(map(int, point_from.split(',')))
        tox, toy = list(map(int, point_to.split(',')))
        if fromx == tox:
            for y in range(min(fromy, toy), max(fromy, toy) + 1):
                walls[(fromx, y)] = True
        elif fromy == toy:
            for x in range(min(fromx, tox), max(fromx, tox) + 1):
                walls[(x, fromy)] = True
        maxY = max(maxY, max(fromy, toy))

maxY += 2

resting = set()

def fill(coord):
    x = coord[0]
    y = coord[1]
    below = (x, y + 1)

    if not walls[below] and below not in resting and below[1] < maxY:
        return fill(below)

    left = (x - 1, y + 1)
    right = (x + 1, y + 1)
    if not walls[left] and left not in resting and left[1] < maxY:
        return fill(left)
    elif not walls[right] and right not in resting and right[1] < maxY:
        return fill(right)

    resting.add((x, y))

    if (x, y) == (500, 0):
        return False

    return True

while fill((500, 0)):
    pass
print(len(resting))