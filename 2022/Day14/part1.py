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

resting = set()

def fill(coord):
    x = coord[0]
    y = coord[1]
    below = (x, y + 1)

    if below[1] > maxY:
        return False

    if not walls[below] and below not in resting:
        return fill(below)

    left = (x - 1, y + 1)
    right = (x + 1, y + 1)
    if not walls[left] and left not in resting:
        return fill(left)
    elif not walls[right] and right not in resting:
        return fill(right)

    resting.add((x, y))

    return True

while fill((500, 0)):
    pass
print(len(resting))