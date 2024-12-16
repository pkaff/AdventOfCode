import heapq
maze = {x + 1j * y: c for y, row in enumerate(open("input.txt", "r").readlines()) for x, c in enumerate(row.strip())}
max_x = max(maze, key=lambda k: k.real).real
max_y = max(maze, key=lambda k: k.imag).imag
start = [pos for pos, val in maze.items() if val == 'S'][0]
end = [pos for pos, val in maze.items() if val == 'E'][0]
maze[end] = '.'
maze[start] = '.'

class Obj:
    def __init__(self, cost, pos, dir):
        self.cost = cost
        self.pos = pos
        self.dir = dir
    def __lt__(self, other):
        return self.cost < other.cost

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

to_visit = [Obj(0, start, dir_to_imag('>'))]
visited = []
while to_visit:
    obj = heapq.heappop(to_visit)
    cur_cost = obj.cost
    cur_pos = obj.pos
    dir = obj.dir
    if cur_pos == end:
        print(cur_cost)
        break
    if (cur_pos, dir) in visited:
        continue
    visited.append((cur_pos, dir))
    for neighbour, n_dir, cost in get_neighbours(cur_pos, dir):
        heapq.heappush(to_visit, Obj(cur_cost + cost, neighbour, n_dir))