from collections import Counter
input = {x + 1j * y : c for y, row in enumerate(open("input.txt", "r").readlines()) for x, c in enumerate(row)}
walls = {pos for pos, val in input.items() if val == '#'}
start = [pos for pos, val in input.items() if val == 'S'][0]
end = [pos for pos, val in input.items() if val == 'E'][0]
max_x = int(max(walls, key=lambda k: k.real).real)
max_y = int(max(walls, key=lambda k: k.imag).imag)
def print_grid(optimal_path, from_pos, to_pos):
    printstr = ''
    for row in range(max_y + 1):
        for col in range(max_x + 1):
            pos = col + 1j * row
            if pos in walls:
                printstr += '#'
            elif pos == from_pos:
                printstr += '1'
            elif pos == to_pos:
                printstr += '2'
            elif pos == start:
                printstr += 'S'
            elif pos == end:
                printstr += 'E'
            elif pos in optimal_path:
                printstr += 'O'
            else:
                printstr += '.'
        printstr += '\n'
    print(printstr)

def in_bounds(pos):
    return pos.real >= 0 and pos.real <= max_x and pos.imag >= 0 and pos.imag <= max_y

def on_track(pos):
    return in_bounds(pos) and pos not in walls

def get_neighbours(pos):
    dirs = [1, -1, -1j, 1j]
    return [pos + dir for dir in dirs if on_track(pos + dir)]

def manhattan_dist(from_pos, to_pos):
    return int(abs(int(from_pos.real) - int(to_pos.real))) + int(abs(int(from_pos.imag) - int(to_pos.imag)))

def get_cheat_neighbours(pos):
    neighbours = []
    for dx in range(-20, 21):
        for dy in range(-20, 21):
            dir = dx + 1j * dy
            new_pos = pos + dir
            dist = manhattan_dist(pos, new_pos)
            if dist <= 20 and on_track(new_pos):
                neighbours.append((new_pos, dist))
    return neighbours

def populate_scores():
    to_visit = [[start]]
    scores = {}
    while to_visit:
        path = to_visit.pop(0)
        cur_pos = path[-1]
        if cur_pos == end:
            scores[cur_pos] = len(path) - 1
            scores = {pos : len(path) - 1 - score for pos, score in scores.items()}
            return path, scores
        if cur_pos in scores:
            continue
        scores[cur_pos] = len(path) - 1
        for neighbour in get_neighbours(cur_pos):
            to_visit.append((path + [neighbour]))
    return [], {}

optimal_path, scores = populate_scores()
count = Counter()
for from_pos in optimal_path:
    for to_pos, shortest_dist in get_cheat_neighbours(from_pos):
        steps_saved = (scores[from_pos] - scores[to_pos]) - shortest_dist
        if steps_saved >= 100:
            count[steps_saved] += 1
print(sum([num for _, num in count.items()]))