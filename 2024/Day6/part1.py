lab = {(x, y): c for y, row in enumerate(open("input.txt", "r").readlines()) for x, c in enumerate(row.strip())}
max_x = max(lab.keys(), key=lambda c: c[0])[0]
max_y = max(lab.keys(), key=lambda c: c[1])[1]
start_pos = list(lab.keys())[list(lab.values()).index('^')]
lab[start_pos] = '.'
def get_next_pos(pos, dir):
    new_dir = dir
    for _ in range(4):
        new_pos = (pos[0] + new_dir[0], pos[1] + new_dir[1])
        if new_pos[0] > max_x or new_pos[0] < 0 or new_pos[1] > max_y or new_pos[1] < 0:
            return None
        if lab[new_pos] == '.':
            return (new_pos, new_dir)
        new_dir = (-new_dir[1], new_dir[0])
    exit("fail")

to_visit = [(start_pos, (0, -1))]
visited = set()
while to_visit:
    pos, dir = to_visit.pop()
    visited.add(pos)
    next_pos = get_next_pos(pos, dir)
    if next_pos:
        to_visit.append(next_pos)
print(len(visited))