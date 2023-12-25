from itertools import combinations

class Coord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, input):
        self.p0, self.v = input.split(' @ ')
        self.p0 = Coord(*list(map(int, self.p0.split(', ')[:-1])))
        self.v = Coord(*list(map(int, self.v.split(', ')[:-1])))
        self.k = self.v.y / self.v.x
        self.m = self.p0.y - self.k * self.p0.x

    def point_is_before(self, point):
        if self.v.x > 0:
            if point.x < self.p0.x:
                return True
        else:
            if point.x > self.p0.x:
                return True
        if self.v.y > 0:
            if point.y < self.p0.y:
                return True
        else:
            if point.y > self.p0.y:
                return True
        return False

def line_intersection(l1, l2):
    if l1.k == l2.k:
        return None

    x = (l1.m - l2.m) / (l2.k - l1.k)
    y = l1.k * x + l1.m

    point = Coord(x, y)

    if l1.point_is_before(point) or l2.point_is_before(point):
        return None

    return x, y

coord_min = 200000000000000
coord_max = 400000000000000
lines = [Line(input.strip()) for input in open("input.txt", "r").readlines()]
num_crossed = 0
for l1, l2 in combinations(lines, 2):
    intersection = line_intersection(l1, l2)
    if intersection:
        x, y = intersection
        if x >= coord_min and x <= coord_max and y >= coord_min and y <= coord_max:
            num_crossed += 1
print(num_crossed)