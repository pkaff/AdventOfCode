import re
from collections import deque
from collections import defaultdict
import sys
def turn(cur_dir, to_turn):
    dirs = ['R', 'D', 'L', 'U']
    if to_turn == 'R':
        return dirs[(dirs.index(cur_dir) + 1) % len(dirs)]
    elif to_turn == 'L':
        return dirs[(dirs.index(cur_dir) - 1) % len(dirs)]
    else:
        assert(False)

def dir_val(dir):
    dirs = ['R', 'D', 'L', 'U']
    return dirs.index(dir)

def get_next_pos_and_dir(col, row, dir):
    next_row = row
    next_col = col
    next_dir = dir
    if dir == 'R':
        next_col += 1
    elif dir == 'D':
        next_row += 1
    elif dir == 'L':
        next_col -= 1
    elif dir == 'U':
        next_row -= 1
    # Top
    if row in range(1, 51) and col in range(51, 101):
        if next_col < 51:
            # Wrap to left side
            next_row = 101 + (50 - row) #row 1 => row 150 and row 50 => row 101
            next_col = 1
            next_dir = 'R'
        elif next_row < 1:
            # Wrap to front side
            next_row = 151 + (col - 51) #col 51 => row 151 and col 100 => row 200
            next_col = 1
            next_dir = 'R'
    # Right
    elif row in range(1, 51) and col in range(101, 151):
        if next_col > 150:
            # Wrap to bottom side
            next_row = 101 + (50 - row) # row 1 => row 150 and row 50 => row 101
            next_col = 100
            next_dir = 'L'
        elif next_row < 1:
            # Wrap to front side
            next_row = 200
            next_col = 1 + (col - 101) #col 101 => 1 and 150 => 50
            next_dir = 'U'
        elif next_row > 50:
            # Wrap to back side
            next_row = 51 + (col - 101) #col 101 => row 51 and col 150 => row 100
            next_col = 100
            next_dir = 'L'
    # Back
    elif row in range(51, 101) and col in range(51, 101):
        if next_col > 100:
            # Wrap to right side
            next_row = 50
            next_col = 101 + (row - 51) #row 51 => col 101 and row 100 => col 150
            next_dir = 'U'
        elif next_col < 51:
            # Wrap to left side
            next_row = 101
            next_col = 1 + (row - 51) #row 51 => col 1 and row 100 => col 50
            next_dir = 'D'
    # Bottom
    elif row in range(101, 151) and col in range(51, 101):
        if next_col > 100:
            # Wrap to right side
            next_row = 50 + (101 - row) #row 150 =>row 1 and row 101 => row 50
            next_col = 150
            next_dir = 'L'
        elif next_row > 150:
            # Wrap to front side
            next_row = 151 + (col - 51) #col 51 => row 151 and col 100 => row 200
            next_col = 50
            next_dir = 'L'
    # Left
    elif row in range(101, 151) and col in range(1, 51):
        if next_row < 101:
            # Wrap to back side
            next_row = 51 + (col - 1) #col 1 => row 51 and col 50 => row 100
            next_col = 51
            next_dir = 'R'
        elif next_col < 1:
            # Wrap to top side
            next_row = 1 + (150 - row) #row 101 => row 50 and row 150 => row 1
            next_col = 51
            next_dir = 'R'
    # Front
    elif row in range(151, 201) and col in range(1, 51):
        if next_col < 1:
            # Wrap to top side
            next_row = 1
            next_col = 51 + (row - 151) #row 200 => col 100 and row 151 => col 51
            next_dir = 'D'
        elif next_col > 50:
            # Wrap to bottom side
            next_row = 150
            next_col = 51 + (row - 151) #row 151 => col 51 and row 200 => col 100
            next_dir = 'U'
        elif next_row > 200:
            # Wrap to right side
            next_row = 1
            next_col = 101 + (col - 1) #col 1 => col 101 and col 50 => col 150
            next_dir = 'D'
    else:
        assert(False)
    return (next_col, next_row), next_dir

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
        next_pos, next_dir = get_next_pos_and_dir(*pos, dir)

        if mymap[next_pos] == '#':
            break
        pos = next_pos
        dir = next_dir
    if turns:
        dir = turn(dir, turns.popleft())

print(1000 * pos[1] + 4* pos[0] + dir_val(dir))