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
if pipes[add_tuples(prev, down)] in ['|', '7', 'F']:
    cur = add_tuples(prev, down)
elif pipes[add_tuples(prev, left)] in ['-', 'L', 'F']:
    cur = add_tuples(prev, left)
elif pipes[add_tuples(prev, up)] in ['|', 'F', '7']:
    cur = add_tuples(prev, up)
elif pipes[add_tuples(prev, right)] in ['-', '7', 'J']:
    cur = add_tuples(prev, right)

visited = [prev]
while pipes[cur] != 'S':
    dir = get_dir(prev, cur)
    prev = cur
    cur = add_tuples(cur, dir)
    visited.append(prev)

print(len(visited)//2)