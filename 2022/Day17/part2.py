from collections import defaultdict
import copy
from itertools import cycle
maxX = 6
occupied = defaultdict(bool)
for x in range(maxX + 1):
    occupied[(x, 0)] = True

class Shape:
    def __init__(self, type):
        if type == 0:
            # '####'
            self.occupied = [(0, 0), (1, 0), (2, 0), (3, 0)]
            self.maxdY = 0
            self.maxdX = 3
        if type == 1:
            # '.#.'
            # '###'
            # '.#.'
            self.occupied = [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]
            self.maxdY = 2
            self.maxdX = 2
        if type == 2:
            # '..#'
            # '..#'
            # '###'
            self.occupied = [(2, 0), (2, 1), (0, 2), (1, 2), (2, 2)]
            self.maxdY = 2
            self.maxdX = 2
        if type == 3:
            # '#'
            # '#'
            # '#'
            # '#'
            self.occupied = [(0, 0), (0, 1), (0, 2), (0, 3)]
            self.maxdY = 3
            self.maxdX = 0
        if type == 4:
            # '##'
            # '##'
            self.occupied = [(0, 0), (1, 0), (0, 1), (1, 1)]
            self.maxdY = 1
            self.maxdX = 1
        self.top_left = [0, 0]
    def set_pos(self, pos):
        self.top_left = pos
    def push(self, dir):
        for dx, dy in self.occupied:
            next_pos = (self.top_left[0] + dx + dir, self.top_left[1] + dy)
            if next_pos[0] > maxX or next_pos[0] < 0 or occupied[next_pos]:
                return
        self.top_left[0] += dir
    def down(self, dir):
        for dx, dy in self.occupied:
            next_pos = (self.top_left[0] + dx, self.top_left[1] + dy + dir)
            if occupied[next_pos]:
                return False
        self.top_left[1] += 1
        return True
    def occupy(self):
        for dx, dy in self.occupied:
            cur_pos = (self.top_left[0] + dx, self.top_left[1] + dy)
            occupied[cur_pos] = True
    def __str__(self):
        ret = ''
        for y in range(self.maxdY + 1):
            for x in range(self.maxdX + 1):
                if (x, y) in self.occupied:
                    ret += '#'
                else:
                    ret += '.'
            ret += '\n'
        ret += "at pos " + str(self.top_left)
        return ret
    def __repr__(self):
        return str(self)

def print_occupied():
    max_occupied_y = min([key[1] for key, value in occupied.items() if value])
    printstr = ""
    for y in range(max_occupied_y, 0):
        for x in range(7):
            if occupied[(x, y)]:
                printstr += '#'
            else:
                printstr += '.'
        printstr += '\n'
    print(printstr)

shapes = [Shape(0), Shape(1), Shape(2), Shape(3), Shape(4)]
input = [1 if c == '>' else -1 for c in open("input.txt", "r").read().strip('\n')]
cur_shape = shapes[0]
next_shape = 1
cur_shape.set_pos([2, -4])
n_shapes_stopped = 0
cached_heights = dict()
input_ix = 0
n_shapes_on_top = 0
total_repeated_height = 0
non_repeated_height = 0
top_height = 0
for dir in cycle(input):
    cur_shape.push(dir)
    if not cur_shape.down(1):
        n_shapes_stopped += 1
        prev_max_occupied_y = min([key[1] for key, value in occupied.items() if value])
        cur_shape.occupy()
        max_occupied_y = min([key[1] for key, value in occupied.items() if value])
        cur_level_str = ''
        for dy in range(6):
            cur_level_str = ''.join(['#' if occupied[x, max_occupied_y + dy] else '.' for x in range(7)])
        key = (next_shape, input_ix, cur_level_str)
        if key in cached_heights:
            #print_occupied()
            print(n_shapes_stopped, max_occupied_y, prev_max_occupied_y, cached_heights[key])
            repeating_shapes = n_shapes_stopped - cached_heights[key][0]
            repeating_height = -(max_occupied_y - cached_heights[key][1])
            n_non_repeated_shapes = (1000000000000 % repeating_shapes)
            total_repeated_height = ((1000000000000 - n_non_repeated_shapes) // repeating_shapes) * repeating_height
            print(n_non_repeated_shapes, cached_heights[key][0] - 1)
            n_shapes_on_top = n_non_repeated_shapes - (cached_heights[key][0] - 1)
            non_repeated_height = -cached_heights[key][2]
            print(repeating_shapes, repeating_height, non_repeated_height)
            print(total_repeated_height, non_repeated_height)
            print(total_repeated_height + non_repeated_height)
            print(key)
            print(n_shapes_on_top)
            #print(cached_heights)
            exit()
        cached_heights[key] = (n_shapes_stopped, max_occupied_y, prev_max_occupied_y)
        cur_shape = copy.copy(shapes[next_shape])
        cur_shape.set_pos([2, max_occupied_y - 3 - 1 - cur_shape.maxdY])
        next_shape = (next_shape + 1) % len(shapes)
    input_ix = (input_ix + 1) % len(input)



# 122797031 too low
# 1590697672463 too low
# 1590697672464
# 1591860468960
# 1590697674416


# right: 1591860465110