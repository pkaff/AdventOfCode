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
for dir in cycle(input):
    cur_shape.push(dir)
    if not cur_shape.down(1):
        cur_shape.occupy()
        cur_shape = copy.copy(shapes[next_shape])
        max_occupied_y = min([key[1] for key, value in occupied.items() if value])
        cur_shape.set_pos([2, max_occupied_y - 3 - 1 - cur_shape.maxdY])
        next_shape = (next_shape + 1) % len(shapes)
        n_shapes_stopped += 1
        if n_shapes_stopped == 2022:
            print(abs(max_occupied_y))
            exit()