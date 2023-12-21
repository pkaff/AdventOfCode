blocked = {complex(x, y): c for y, row in enumerate(open("input.txt", "r").readlines()) for x, c in enumerate(row.strip()) if c == '#' or c == 'S'}
start = list(blocked.keys())[list(blocked.values()).index('S')]

def get_neighbours(pos):
    dirs = [1, -1, 1j, -1j]
    return [pos + dir for dir in dirs if (pos + dir) not in blocked]

visited = []
to_visit = [(start, 0)]
tiles_reachable = 0
while to_visit:
    cur, depth = to_visit.pop(0)
    if depth == 64 + 1:
        break
    if depth % 2 == 0:
        tiles_reachable += 1
    for next in get_neighbours(cur):
        if next not in visited:
            to_visit.append((next, depth + 1))
            visited.append(next)

print(tiles_reachable)