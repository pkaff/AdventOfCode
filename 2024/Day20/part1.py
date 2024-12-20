from collections import Counter
input = {x + 1j * y : c for y, row in enumerate(open("input.txt", "r").readlines()) for x, c in enumerate(row)}
walls = {pos for pos, val in input.items() if val == '#'}
start = [pos for pos, val in input.items() if val == 'S'][0]
end = [pos for pos, val in input.items() if val == 'E'][0]
max_x = int(max(walls, key=lambda k: k.real).real)
max_y = int(max(walls, key=lambda k: k.imag).imag)
def print_grid(cur_pos, cheat_pos, end_pos, optimal_path):
    printstr = ''
    for row in range(max_y + 1):
        for col in range(max_x + 1):
            pos = col + 1j * row
            if pos == cheat_pos[0]:
                printstr += '1'
            elif pos == cheat_pos[1]:
                printstr += '2'
            elif pos in walls:
                printstr += '#'
            elif pos == cur_pos:
                printstr += '@'
            elif pos == end_pos:
                printstr += 'T'
            elif pos in optimal_path:
                printstr += 'O'
            else:
                printstr += '.'
        printstr += '\n'
    print(printstr)

def in_bounds(pos):
    return pos.real >= 0 and pos.real <= max_x and pos.imag >= 0 and pos.imag <= max_y

def get_neighbours(pos, cheat):
    dirs = [1, -1, -1j, 1j]
    return [pos + dir for dir in dirs if in_bounds(pos + dir) and (cheat or pos + dir not in walls)]

def get_cheat_neighbours(cur_pos):
    neighbours1 = set(get_neighbours(cur_pos, True))
    neighbours2 = set()
    for neighbour in neighbours1:
        neighbours2 |= set(get_neighbours(neighbour, False))
    return neighbours2

def find_path(cheat):
    to_visit = [([start], 2)]
    visited = []
    while to_visit:
        path, cheats_left = to_visit.pop(0)
        cur_pos = path[-1]
        if cur_pos == end:
            return path
        if (cur_pos, cheats_left) in visited:
            continue
        visited.append((cur_pos, cheats_left))
        for neighbour in get_neighbours(cur_pos, False):
            to_visit.append((path + [neighbour], cheats_left))
        if cheat and cheats_left > 0:
            for neighbour in get_neighbours(cur_pos, True):
                to_visit.append((path + [neighbour], cheats_left - 1))
    return []

optimal_path = find_path(False)
count = Counter()
for from_ix, pos in enumerate(optimal_path):
    cheat_neighbours = get_cheat_neighbours(pos)
    for neighbour in cheat_neighbours:
        to_ix = optimal_path.index(neighbour)
        steps_saved = to_ix - (from_ix + 2)
        if steps_saved > 0:
            count[steps_saved] += 1
print(sum([num for saved, num in count.items() if saved >= 100]))