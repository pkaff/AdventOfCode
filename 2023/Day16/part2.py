mirrors = {(x, y): c for y, row in enumerate(open("input.txt", "r").readlines()) for x, c in enumerate(row.strip())}
max_x = max(mirrors.keys(), key=lambda c: c[0])[0]
max_y = max(mirrors.keys(), key=lambda c: c[1])[1]

def get_next_pos(pos, dirs):
    ret = []
    for dir in dirs:
        new_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if new_pos[0] <= max_x and new_pos[0] >= 0 and new_pos[1] <= max_y and new_pos[1] >= 0:
            ret.append((new_pos, dir))
    return ret

def get_nexts_to_visit(pos, dir):
    c = mirrors[pos]
    dirs = []
    if c == '.' or (c == '|' and dir[0] == 0) or (c == '-' and dir[1] == 0):
        dirs.append(dir)
    elif c == '/':
        dirs.append((-dir[1], -dir[0]))
    elif c == '\\':
        dirs.append((dir[1], dir[0]))
    elif c == '|':
        dirs = [(0, -1), (0, 1)]
    elif c == '-':
        dirs = [(1, 0), (-1, 0)]
    return get_next_pos(pos, dirs)

def get_energized(init_pos, init_dir):
    to_visit = [(init_pos, init_dir)]
    visited = set()
    while to_visit:
        pos, dir = to_visit.pop()
        if (pos, dir) in visited:
            continue
        visited.add((pos, dir))
        nexts = get_nexts_to_visit(pos, dir)
        to_visit += nexts
    return len({pos for pos, _ in visited})

energized = []
for x in range(max_x + 1):
    energized.append(get_energized((x, 0), (0, 1)))
    energized.append(get_energized((x, max_y), (0, -1)))
for y in range(max_y + 1):
    energized.append(get_energized((0, y), (1, 0)))
    energized.append(get_energized((max_x, y), (-1, 0)))
print(max(energized))