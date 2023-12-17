import heapq
import itertools
import sys
from collections import defaultdict
counter = itertools.count()
blocks = {complex(x, y): int(c) for y, row in enumerate(open("input.txt", "r").readlines()) for x, c in enumerate(row.strip())}
max_x = max(blocks.keys(), key=lambda c: c.real).real
max_y = max(blocks.keys(), key=lambda c: c.imag).imag

def get_neighbours(pos, dirs):
    neighbours = []
    cur_dir = dirs[-1]

    if len(dirs) < 3 or not all(d == cur_dir for d in dirs[-3:]):
        new_pos = pos + cur_dir
        if new_pos in blocks:
            neighbours.append((new_pos, cur_dir))

    left_dir = complex(cur_dir.imag, -cur_dir.real)
    new_pos_l = pos + left_dir
    if new_pos_l in blocks:
        neighbours.append((new_pos_l, left_dir))

    right_dir = complex(-cur_dir.imag, cur_dir.real)
    new_pos_r = pos + right_dir
    if new_pos_r in blocks:
        neighbours.append((new_pos_r, right_dir))

    return neighbours

def to_key(pos, dirs):
    return str(pos) + str(dirs)

queue = []
best_heat_loss = defaultdict(lambda: sys.maxsize)
best_heat_loss[to_key(0 + 0j, [1 + 0j])] = 0
heapq.heappush(queue, (0, next(counter), 0 + 0j, [1 + 0j]))
while queue:
    heat_loss, _, pos, dirs = heapq.heappop(queue)
    if pos == complex(max_x, max_y):
        print(heat_loss)
        break
    neighbours = get_neighbours(pos, dirs)
    for n_pos, n_dir in neighbours:
        next_heat_loss = heat_loss + blocks[n_pos]
        n_dirs = dirs + [n_dir]
        n_key = to_key(n_pos, n_dirs[-3:])
        if next_heat_loss < best_heat_loss[n_key]:
            best_heat_loss[n_key] = next_heat_loss
            heapq.heappush(queue, (next_heat_loss, next(counter), n_pos, n_dirs))