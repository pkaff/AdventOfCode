import heapq
import itertools
counter = itertools.count()
blocks = {complex(x, y): int(c) for y, row in enumerate(open("input.txt", "r").readlines()) for x, c in enumerate(row.strip())}
max_x = max(blocks.keys(), key=lambda c: c.real).real
max_y = max(blocks.keys(), key=lambda c: c.imag).imag

def get_dirs(cur_dir):
    left_dir = complex(cur_dir.imag, -cur_dir.real)
    right_dir = complex(-cur_dir.imag, cur_dir.real)

    return [left_dir, right_dir, cur_dir]

queue = []
visited = set()
heapq.heappush(queue, (0, next(counter), 0, 0 + 0j, 1 + 0j))
heapq.heappush(queue, (0, next(counter), 0, 0 + 0j, 0 + 1j))
while queue:
    heat_loss, _, n_steps, pos, dir = heapq.heappop(queue)
    if pos == complex(max_x, max_y):
        if n_steps >= 4:
            print(heat_loss)
            break
        continue

    if (pos, n_steps, dir) in visited:
        continue

    visited.add((pos, n_steps, dir))

    new_dirs = get_dirs(dir)
    for n_dir in new_dirs:
        is_straight = n_dir == dir
        n_pos = pos + n_dir
        if n_pos not in blocks:
            continue
        if n_steps == 10 and is_straight:
            continue
        if n_steps < 4 and not is_straight:
            continue
        n_n_steps = n_steps + 1 if is_straight else 1
        next_heat_loss = heat_loss + blocks[n_pos]
        heapq.heappush(queue, (next_heat_loss, next(counter), n_n_steps, n_pos, n_dir))