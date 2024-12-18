inputs = [int(row.strip().split(',')[0]) + 1j * int(row.strip().split(',')[1]) for row in open("input.txt", "r").readlines()]
max_x = 70
max_y = 70
start = 0
end = max_x + 1j * max_y
print(inputs[:1024])
def in_bounds(pos):
    return pos not in inputs[:1024] and pos.imag >= 0 and pos.imag <= max_y and pos.real >= 0 and pos.real <= max_x

def print_path(path):
    print_str = ''
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            pos = x + 1j * y
            if pos in path:
                print_str += 'O'
            elif in_bounds(pos):
                print_str += '.'
            else:
                print_str += '#'
        print_str += '\n'
    print(print_str)

def get_neighbours(pos):
    dirs = [1, -1, -1j, 1j]
    neighbours = [pos + dir for dir in dirs if in_bounds(pos + dir)]
    return neighbours

to_visit = [([start])]
visited = []
while to_visit:
    path = to_visit.pop(0)
    cur_pos = path[-1]
    if cur_pos == end:
        print_path(path)
        print(len(path) - 1)
        break
    if cur_pos in visited:
        continue
    visited.append(cur_pos)
    for neighbour in get_neighbours(cur_pos):
        to_visit.append((path + [neighbour]))