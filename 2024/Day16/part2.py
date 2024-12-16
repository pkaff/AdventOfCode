import heapq
import sys
from collections import defaultdict
maze = {x + 1j * y: c for y, row in enumerate(open("input.txt", "r").readlines()) for x, c in enumerate(row.strip())}
max_x = max(maze, key=lambda k: k.real).real
max_y = max(maze, key=lambda k: k.imag).imag
start = [pos for pos, val in maze.items() if val == 'S'][0]
end = [pos for pos, val in maze.items() if val == 'E'][0]
maze[end] = '.'
maze[start] = '.'

class Obj:
    def __init__(self, cost, pos, dir, path):
        self.cost = cost
        self.pos = pos
        self.dir = dir
        self.path = path
    def __lt__(self, other):
        return self.cost < other.cost
    def __repr__(self):
        return f'({self.cost}, {self.pos}, {self.dir})'
def dir_to_imag(dir):
    if dir == '^':
        return -1j
    if dir == '>':
        return 1
    if dir == '<':
        return -1
    if dir == 'v':
        return 1j

def in_bounds(pos):
    return maze[pos] == '.'

def get_neighbours(pos, dir):
    neighbours = []
    if in_bounds(pos + dir):
        neighbours.append((pos + dir, dir, 1))
    if in_bounds(pos + dir * -1j):
        neighbours.append((pos + dir * -1j, dir * -1j, 1001))
    if in_bounds(pos + dir * 1j):
        neighbours.append((pos + dir * 1j, dir * 1j, 1001))
    if in_bounds(pos + dir * -1):
        neighbours.append((pos + dir * -1, dir * -1, 2001))
    return neighbours

to_visit = [Obj(0, start, dir_to_imag('>'), set([start]))]
best_costs = defaultdict(lambda: sys.maxsize)
while to_visit:
    obj = heapq.heappop(to_visit)
    cur_cost = obj.cost
    cur_pos = obj.pos
    dir = obj.dir
    path = obj.path
    if cur_pos == end:
        best_cost = cur_cost
        pos_on_path = set(path)
        while cur_cost == best_cost:
            pos_on_path |= path
            obj = heapq.heappop(to_visit)
            cur_cost = obj.cost
            cur_pos = obj.pos
            dir = obj.dir
            path = obj.path
        print(len(pos_on_path))
        break
    if cur_cost > best_costs[(cur_pos, dir)]:
        continue
    best_costs[(cur_pos, dir)] = cur_cost
    for neighbour, n_dir, cost in get_neighbours(cur_pos, dir):
        heapq.heappush(to_visit, Obj(cur_cost + cost, neighbour, n_dir, path | set([neighbour])))