garden = {(x, y): c for y, row in enumerate(open("input.txt", "r").readlines()) for x, c in enumerate(row.strip())}
max_x = max(garden.keys(), key=lambda c: c[0])[0]
max_y = max(garden.keys(), key=lambda c: c[1])[1]
visited = set()
cost = 0
def point_in_bounds_and_same_plot(pos, c):
    return pos[0] >= 0 and pos[0] <= max_x and pos[1] >= 0 and pos[1] <= max_y and c == garden[pos]

def get_neighbours(pos, c):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    return [(pos[0] + dir[0], pos[1] + dir[1]) for dir in dirs if point_in_bounds_and_same_plot((pos[0] + dir[0], pos[1] + dir[1]), c)]

for x in range(max_x + 1):
    for y in range(max_y + 1):
        if (x, y) in visited:
            continue
        area = 0
        perimiter = 0
        to_visit = [(x, y)]
        c = garden[(x, y)]
        while to_visit:
            pos = to_visit.pop()
            if pos in visited:
                continue
            visited.add(pos)
            area += 1
            neighbours = get_neighbours(pos, c)
            perimiter += 4 - len(neighbours)
            to_visit.extend(neighbours)
        cost += area * perimiter
print(cost)