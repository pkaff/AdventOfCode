garden = {(x, y): c for y, row in enumerate(open("input.txt", "r").readlines()) for x, c in enumerate(row.strip())}
max_x = max(garden.keys(), key=lambda c: c[0])[0]
max_y = max(garden.keys(), key=lambda c: c[1])[1]
for x in [-1, max_x + 1]:
    for y in range(-1, max_y + 2):
        garden[(x, y)] = '.'
for y in [-1, max_y + 1]:
    for x in range(-1, max_x + 2):
        garden[(x, y)] = '.'

visited = set()
cost = 0

def get_neighbours(pos, c):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    return [add(pos, dir) for dir in dirs if garden[add(pos, dir)] == c]

def add(pos, dir):
    return (pos[0] + dir[0], pos[1] + dir[1])

def count_corners(pos, c):
    corners = 0
    # normal corners
    if garden[add(pos, (0, -1))] != c and garden[add(pos, (1, 0))] != c:
        corners += 1
    if garden[add(pos, (0, -1))] != c and garden[add(pos, (-1, 0))] != c:
        corners += 1
    if garden[add(pos, (0, 1))] != c and garden[add(pos, (1, 0))] != c:
        corners += 1
    if garden[add(pos, (0, 1))] != c and garden[add(pos, (-1, 0))] != c:
        corners += 1

    # 'negative' corners
    if garden[add(pos, (0, -1))] == c and garden[add(pos, (-1, 0))] == c and garden[add(pos, (-1, -1))] != c:
        corners += 1
    if garden[add(pos, (0, -1))] == c and garden[add(pos, (1, 0))] == c and garden[add(pos, (1, -1))] != c:
        corners += 1
    if garden[add(pos, (0, 1))] == c and garden[add(pos, (-1, 0))] == c and garden[add(pos, (-1, 1))] != c:
        corners += 1
    if garden[add(pos, (0, 1))] == c and garden[add(pos, (1, 0))] == c and garden[add(pos, (1, 1))] != c:
        corners += 1

    return corners

for x in range(max_x + 1):
    for y in range(max_y + 1):
        if (x, y) in visited:
            continue
        area = 0
        corners = 0
        to_visit = [(x, y)]
        c = garden[(x, y)]
        while to_visit:
            pos = to_visit.pop()
            if pos in visited:
                continue
            visited.add(pos)
            area += 1
            neighbours = get_neighbours(pos, c)
            corners += count_corners(pos, c)
            to_visit.extend(neighbours)
        cost += area * corners
print(cost)