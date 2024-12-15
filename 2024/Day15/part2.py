map, moves = open("input.txt", "r").read().split('\n\n')
map = map.split('\n')
walls = {2 * x + i + 1j * y for y, row in enumerate(map) for x, c in enumerate(row) for i in range(2) if c == '#'}
boxes = {(2 * x + 1j * y, 2 * x + 1 + 1j * y) for y, row in enumerate(map) for x, c in enumerate(row) if c == 'O'}
pos = [2 * x + 1j * y for y, row in enumerate(map) for x, c in enumerate(row) if c == '@'][0]
moves = moves.replace('\n','').strip()
def dir_to_imag(dir):
    if dir == '^':
        return -1j
    if dir == '>':
        return 1
    if dir == '<':
        return -1
    if dir == 'v':
        return 1j

def get_box(pos):
    return next(filter(lambda box: box[0] == pos or box[1] == pos, boxes), None)

def print_grid(cur_pos):
    printstr = ''
    for row in range(len(map[0])):
        for col in range(2 * len(map)):
            pos = col + 1j * row
            if pos in walls:
                printstr += '#'
            elif pos == cur_pos:
                printstr += '@'
            elif get_box(pos):
                box = get_box(pos)
                if pos == box[0]:
                    printstr += '['
                else:
                    printstr += ']'
            else:
                printstr += '.'
        printstr += '\n'
    print(printstr)

def is_movable(pos, boxes_in_row, dir):
    return pos + dir not in walls if len(boxes_in_row) == 0 else not any([box[0] + dir in walls or box[1] + dir in walls for box in boxes_in_row])

def get_boxes_in_row(pos, dir):
    boxes_in_row = []
    pos += dir
    boxes_to_visit = [get_box(pos)]
    while boxes_to_visit:
        box = boxes_to_visit.pop()
        if box and box not in boxes_in_row:
            boxes_in_row.append(box)
            boxes_to_visit.append(get_box(box[0] + dir))
            boxes_to_visit.append(get_box(box[1] + dir))

    return boxes_in_row

for dir in moves:
    dir = dir_to_imag(dir)
    boxes_to_move = get_boxes_in_row(pos, dir)
    if is_movable(pos, boxes_to_move, dir):
        pos += dir
        moved_boxes = {(box[0] + dir, box[1] + dir) for box in boxes_to_move}
        for box in boxes_to_move:
            boxes.remove(box)
        for moved_box in moved_boxes:
            boxes.add(moved_box)

print(int(sum([100 * pos[0].imag + pos[0].real for pos in boxes])))