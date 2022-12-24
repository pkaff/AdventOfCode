from collections import deque
from collections import Counter

elves_pos = set((row, col) for row, line in enumerate(open("input.txt", "r").readlines()) for col, c in enumerate(line) if c == '#')
num_elves = len(elves_pos)

def none_north(pos):
    return all([(pos[0] - 1, pos[1]) not in elves_pos, (pos[0] - 1, pos[1] - 1) not in elves_pos, (pos[0] - 1, pos[1] + 1) not in elves_pos])

def none_south(pos):
    return all([(pos[0] + 1, pos[1]) not in elves_pos, (pos[0] + 1, pos[1] - 1) not in elves_pos, (pos[0] + 1, pos[1] + 1) not in elves_pos])

def none_west(pos):
    return all([(pos[0] - 1, pos[1] - 1) not in elves_pos, (pos[0], pos[1] - 1) not in elves_pos, (pos[0] + 1, pos[1] - 1) not in elves_pos])

def none_east(pos):
    return all([(pos[0] - 1, pos[1] + 1) not in elves_pos, (pos[0], pos[1] + 1) not in elves_pos, (pos[0] + 1, pos[1] + 1) not in elves_pos])

def no_neighbours(pos):
    return all([none_north(pos), none_south(pos), none_west(pos), none_east(pos)])

def next_pos(pos, next_move):
    for next_move_fun in next_move:
        next_pos = next_move_fun(pos)
        if next_pos:
            return next_pos
    return pos

def print_elves():
    maxRow = max([pos[0] for pos in elves_pos])
    minRow = min([pos[0] for pos in elves_pos])
    maxCol = max([pos[1] for pos in elves_pos])
    minCol = min([pos[1] for pos in elves_pos])
    printstr = ''
    for row in range(minRow, maxRow + 1):
        for col in range(minCol, maxCol + 1):
            if (row, col) in elves_pos:
                printstr += '#'
            else:
                printstr += '.'
        printstr += '\n'
    print(printstr)

next_move = deque([lambda pos: (pos[0] - 1, pos[1]) if none_north(pos) else None, lambda pos: (pos[0] + 1, pos[1]) if none_south(pos) else None, lambda pos: (pos[0], pos[1] - 1) if none_west(pos) else None, lambda pos: (pos[0], pos[1] + 1) if none_east(pos) else None])
for round in range(10):
    proposed_moves = [(pos, next_pos(pos, next_move)) for pos in elves_pos if not no_neighbours(pos)]
    unique_moves = set(k for k, v in Counter([p[1] for p in proposed_moves]).items() if v == 1)
    for pos_from, pos_to in proposed_moves:
        if pos_to in unique_moves:
            elves_pos.remove(pos_from)
            elves_pos.add(pos_to)
    next_move.rotate(-1)
    assert(num_elves == len(elves_pos))
maxRow = max([pos[0] for pos in elves_pos])
minRow = min([pos[0] for pos in elves_pos])
maxCol = max([pos[1] for pos in elves_pos])
minCol = min([pos[1] for pos in elves_pos])
print((maxRow + 1 - minRow) * (maxCol + 1 - minCol) - len(elves_pos))