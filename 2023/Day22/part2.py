from collections import defaultdict
from functools import lru_cache
class Coord:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def __str__(self):
        return f'{self.x},{self.y}'
    def __repr__(self):
        return str(self)

class Brick:
    def __init__(self, c1, c2):
        x1, y1, z1 = c1.split(',')
        x2, y2, z2 = c2.split(',')
        self.c1 = Coord(x1, y1)
        self.c2 = Coord(x2, y2)
        self.z = min(int(z1), int(z2))
        self.height = max(int(z1), int(z2)) - self.z + 1

    def fall(self, overview):
        if self.min_z() == 1:
            for c in self.get_coords():
                overview[c] = self.max_z()
        else:
            z = 0
            for c in self.get_coords():
                if c in overview:
                    z = max(z, overview[c])
            self.z = z + 1
            for c in self.get_coords():
                overview[c] = self.max_z()

    def get_coords(self):
        return [Coord(x, y) for x in range(self.min_x(), self.max_x() + 1) for y in range(self.min_y(), self.max_y() + 1)]

    def overlaps_xy(self, other):
        s_minx = min(self.c1.x, self.c2.x)
        s_maxx = max(self.c1.x, self.c2.x)
        s_miny = min(self.c1.y, self.c2.y)
        s_maxy = max(self.c1.y, self.c2.y)

        o_minx = min(other.c1.x, other.c2.x)
        o_maxx = max(other.c1.x, other.c2.x)
        o_miny = min(other.c1.y, other.c2.y)
        o_maxy = max(other.c1.y, other.c2.y)

        left_intersect = max(s_minx, o_minx)
        top_intersect = max(s_miny, o_miny)
        right_intersect = min(s_maxx, o_maxx)
        bottom_intersect = min(s_maxy, o_maxy)

        return left_intersect <= right_intersect and top_intersect <= bottom_intersect

    def min_x(self):
        return min(self.c1.x, self.c2.x)

    def max_x(self):
        return max(self.c1.x, self.c2.x)

    def min_y(self):
        return min(self.c1.y, self.c2.y)

    def max_y(self):
        return max(self.c1.y, self.c2.y)

    def min_z(self):
        return self.z

    def max_z(self):
        return self.z + self.height - 1

    def __str__(self):
        return f'{self.c1},{self.min_z()}~{self.c2},{self.max_z()}'
    def __repr__(self):
        return str(self)

bricks = [Brick(*line.strip().split('~')) for line in open("input.txt", "r").readlines()]
bricks.sort(key=lambda b: b.min_z())
overview = {}
for brick in bricks:
    brick.fall(overview)

bricks.sort(key=lambda b: b.min_z())
supported_by = defaultdict(lambda: [])
supportings = defaultdict(lambda: [])
for ix, brick in enumerate(bricks):
    supported_bricks = [b for b in bricks[ix + 1:] if b.min_z() == brick.max_z() + 1 and brick.overlaps_xy(b)]
    for supported_brick in supported_bricks:
        supported_by[supported_brick].append(brick)
        supportings[brick].append(supported_brick)

sole_support = set()
for brick, supporting in supported_by.items():
    if len(supporting) == 1:
        sole_support.add(supporting[0])

num_falling = 0
for brick in sole_support:
    to_remove = [brick]
    removed = []
    while to_remove:
        next = to_remove.pop()
        removed.append(next)
        for supported_brick in supportings[next]:
            if all(sb in removed for sb in supported_by[supported_brick]):
                to_remove.append(supported_brick)
    num_falling += len(removed) - 1

print(num_falling)