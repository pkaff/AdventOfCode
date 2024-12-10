mountain = {(x, y): int(c) for y, row in enumerate(open("input.txt", "r").readlines()) for x, c in enumerate(row.strip())}
max_x = max(mountain, key=lambda k: k[0])[0]
max_y = max(mountain, key=lambda k: k[1])[1]
starts = [key for key, val in mountain.items() if val == 0]

def point_in_bounds(pos):
    return pos[0] >= 0 and pos[0] <= max_x and pos[1] >= 0 and pos[1] <= max_y

def get_neighbours(cur):
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    return [(cur[0] + dir[0], cur[1] + dir[1]) for dir in dirs if point_in_bounds((cur[0] + dir[0], cur[1] + dir[1]))]     

score = 0
for start in starts:
    to_visit = [start]
    tops = set()
    while to_visit:
        cur = to_visit.pop()
        if mountain[cur] == 9:
            tops.add(cur)
            continue
        for neighbour in get_neighbours(cur):
            next_c = mountain[neighbour]
            if next_c == mountain[cur] + 1:
                to_visit.append(neighbour)
    score += len(tops)
print(score)