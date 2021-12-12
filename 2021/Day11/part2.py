myin = {(x, y): int(c) for (y, line) in enumerate(open("input.txt", "r").readlines()) for (x, c) in enumerate(line.replace('\n', ''))}
maxX = max([x for (x, y) in myin.keys()])
maxY = max([y for (x, y) in myin.keys()])
def get_neighbours(x, y):
    indices = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x - 1, y), (x + 1, y), (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
    neighbours = []
    for (xx, yy) in indices:
        if xx >= 0 and xx <= maxX and yy >= 0 and yy <= maxY:
            neighbours.append((xx, yy))
    return neighbours
ix = 1
while True:
    myin = {key: val + 1 for key, val in myin.items()}
    flashed = [key for key, val in myin.items() if val > 9]
    visited = flashed[:]
    while flashed:
        (x, y) = flashed.pop()
        neighbours = get_neighbours(x, y)
        for neighbour in neighbours:
            myin[neighbour] += 1
            if myin[neighbour] > 9 and neighbour not in visited:
                visited.append(neighbour)
                flashed.append(neighbour)
    if len(visited) == len(myin):
        print(ix)
        break
    myin = {key: val if val <= 9 else 0 for key, val in myin.items()}
    ix += 1


