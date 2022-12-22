import re
from collections import deque
from collections import defaultdict
import sys
def turn(cur_dir, to_turn):
    dirs = ['R', 'D', 'L', 'U']
    if to_turn == 'R':
        return dirs[(dirs.index(cur_dir) + 1) % len(dirs)]
    if to_turn == 'L':
        return dirs[(dirs.index(cur_dir) - 1) % len(dirs)]

def dir_val(dir):
    dirs = ['R', 'D', 'L', 'U']
    return dirs.index(dir)

input_map, input_path = open("input.txt", "r").read().split('\n\n')
mymap = {(col + 1, row + 1): c for row, line in enumerate(input_map.split('\n')) for col, c in enumerate(line) if c != ' '}

steps = deque(map(int, re.findall(r'\d+', input_path)))
turns = deque(re.findall(r'(R|L)', input_path))

row_mins = defaultdict(lambda: int(sys.maxsize))
row_maxs = defaultdict(lambda: 0)
col_mins = defaultdict(lambda: int(sys.maxsize))
col_maxs = defaultdict(lambda: 0)
max_col = max(mymap.keys(), key=lambda key: key[0])[0]
max_row = max(mymap.keys(), key=lambda key: key[1])[1]
for col in range(1, max_col + 1):
    for row in range(1, max_row + 1):
        if (col, row) in mymap:
            row_mins[row] = min(row_mins[row], col)
            row_maxs[row] = max(row_maxs[row], col)
            col_mins[col] = min(col_mins[col], row)
            col_maxs[col] = max(col_maxs[col], row)

pos = min([pos for pos in mymap.keys() if pos[1] == 1 and mymap[pos] == '.'], key=lambda key: key[0])
dir = 'R'
for step in steps:
    for _ in range(step):
        col, row = pos

        next_row = row
        next_col = col

        if dir == 'R':
            next_col += 1
            if next_col > row_maxs[row]:
                next_col = row_mins[row]
        elif dir == 'D':
            next_row += 1
            if next_row > col_maxs[col]:
                next_row = col_mins[col]
        elif dir == 'L':
            next_col -= 1
            if next_col < row_mins[row]:
                next_col = row_maxs[row]
        elif dir == 'U':
            next_row -= 1
            if next_row < col_mins[col]:
                next_row = col_maxs[col]

        next_pos = (next_col, next_row)
        if mymap[next_pos] == '#':
            break
        pos = next_pos
    if turns:
        dir = turn(dir, turns.popleft())

print(1000 * pos[1] + 4* pos[0] + dir_val(dir))