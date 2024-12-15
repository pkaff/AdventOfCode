map, moves = open("input.txt", "r").read().split('\n\n')
map = map.split('\n')
walls = {x + 1j * y for y, row in enumerate(map) for x, c in enumerate(row) if c == '#'}
boxes = {x + 1j * y for y, row in enumerate(map) for x, c in enumerate(row) if c == 'O'}
pos = [x + 1j * y for y, row in enumerate(map) for x, c in enumerate(row) if c == '@'][0]
moves = moves.replace('\n','').strip()

def print_grid(cur_pos):
    printstr = ''
    for row in range(len(map[0])):
        for col in range(len(map)):
            pos = col + 1j * row
            if pos in walls:
                printstr += '#'
            elif pos == cur_pos:
                printstr += '@'
            elif pos in boxes:
                printstr += 'O'
            else:
                printstr += '.'
        printstr += '\n'
    print(printstr)

def dir_to_imag(dir):
    if dir == '^':
        return -1j
    if dir == '>':
        return 1
    if dir == '<':
        return -1
    if dir == 'v':
        return 1j

def is_movable(pos, boxes_in_row, dir):
    return pos + dir not in walls if len(boxes_in_row) == 0 else boxes_in_row[-1] + dir not in walls

def get_boxes_in_row(pos, dir):
    boxes_in_row = []
    pos += dir
    while pos in boxes:
        boxes_in_row.append(pos)
        pos += dir
    return boxes_in_row

for dir in moves:
    dir = dir_to_imag(dir)
    boxes_to_move = get_boxes_in_row(pos, dir)
    if is_movable(pos, boxes_to_move, dir):
        pos += dir
        if len(boxes_to_move) == 1:
            boxes.add(boxes_to_move[-1] + dir)
            boxes.remove(boxes_to_move[-1])
        elif len(boxes_to_move) > 1:
            boxes.add(boxes_to_move[-1] + dir)
            boxes.remove(boxes_to_move[0])

print(int(sum([100 * pos.imag + pos.real for pos in boxes])))