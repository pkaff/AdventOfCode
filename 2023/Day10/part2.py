from collections import defaultdict
from operator import add

down, up, right, left = [(0, 1), (0, -1), (1, 0), (-1, 0)]
pipes = defaultdict(lambda: '.', {(x, y): c for y, row in enumerate(open("input.txt", "r").readlines()) for x, c in enumerate(row.strip())})

def add_tuples(t1, t2):
    return tuple(map(add, t1, t2))

def get_dir(prev_pos, cur_pos):
    c = pipes[cur_pos]
    if c == '-':
        if prev_pos[0] < cur_pos[0]:
            return right
        else:
            return left
    if c == '|':
        if prev_pos[1] < cur_pos[1]:
            return down
        else:
            return up
    if c == 'L':
        if prev_pos[1] < cur_pos[1]:
            return right
        else:
            return up
    if c == 'J':
        if prev_pos[1] < cur_pos[1]:
            return left
        else:
            return up
    if c == '7':
        if prev_pos[1] > cur_pos[1]:
            return left
        else:
            return down
    if c == 'F':
        if prev_pos[1] > cur_pos[1]:
            return right
        else:
            return down
    exit()
prev = list(pipes.keys())[list(pipes.values()).index('S')]
cur = ()
potential_s = set()
if pipes[add_tuples(prev, down)] in ['|', 'J', 'L']:
    cur = add_tuples(prev, down)
    potential_s = {'7', 'F', '|'}
elif pipes[add_tuples(prev, left)] in ['-', 'L', 'F']:
    cur = add_tuples(prev, left)
    potential_s = {'7', 'J', '-'}
elif pipes[add_tuples(prev, up)] in ['|', 'F', '7']:
    cur = add_tuples(prev, up)
    potential_s = {'L', 'J', '|'}
elif pipes[add_tuples(prev, right)] in ['-', '7', 'J']:
    cur = add_tuples(prev, right)
    potential_s = {'F', '-', 'L'}

loop = [prev]
while pipes[cur] != 'S':
    dir = get_dir(prev, cur)
    prev = cur
    cur = add_tuples(cur, dir)
    loop.append(prev)
if loop[0][0] > loop[-1][0]:
    potential_s -= {'|', 'L', 'F'}
elif loop[0][0] < loop[-1][0]:
    potential_s -= {'|', '7', 'J'}
elif loop[0][1] > loop[-1][1]:
    potential_s -= {'-', '7', 'F'}
elif loop[0][1] < loop[-1][1]:
    potential_s -= {'-', 'L', 'J'}
pipes[loop[0]] = potential_s.pop()
max_x = max(loop, key=lambda t: t[0])[0]
min_x = min(loop, key=lambda t: t[0])[0]
max_y = max(loop, key=lambda t: t[1])[1]
min_y = min(loop, key=lambda t: t[1])[1]

pos_inside = []
for x in range(min_x, max_x + 1):
    is_inside = False
    num_corners = {'F': 0, 'J': 0, '7': 0, 'L': 0}
    for y in range(min_y, max_y + 1):
        pos = (x, y)
        if pos in loop:
            c = pipes[pos]
            if c == '-':
                is_inside = not is_inside
            elif c != '|':
                num_corners[c] += 1
                if num_corners['F'] >= 1 and num_corners['J'] >= 1:
                    is_inside = not is_inside
                    num_corners['F'] -= 1
                    num_corners['J'] -= 1
                elif num_corners['L'] >= 1 and num_corners['7'] >= 1:
                    is_inside = not is_inside
                    num_corners['L'] -= 1
                    num_corners['7'] -= 1
        elif is_inside:
            pos_inside.append(pos)
print(len(pos_inside))

def print_graph():
    for y in range(min_y, max_y + 1):
        line = ""
        for x in range(min_x, max_x + 1):
            pos = (x, y)
            if pos in loop:
                line += pipes[pos]
            elif pos in pos_inside:
                line += 'I'
            else:
                line += 'O'
        print(line)