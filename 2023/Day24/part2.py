from itertools import combinations

class Coord:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Line:
    def __init__(self, input):
        self.p0, self.v = input.split(' @ ')
        self.p0 = Coord(*list(map(int, self.p0.split(', '))))
        self.v = Coord(*list(map(int, self.v.split(', '))))

lines = [Line(input.strip()) for input in open("input.txt", "r").readlines()]

def calc_potential_set(l1_v, l1_p, l2_p, potential_set):
    new_set = set()
    diff = l2_p - l1_p
    for v in range(-1000, 1000):
        if v == l1_v:
            continue
        if diff % (v - l1_v) == 0:
            new_set.add(v)
    if potential_set != None:
        potential_set = potential_set & new_set
    else:
        potential_set = new_set.copy()
    return potential_set

potential_x_set = None
potential_y_set = None
potential_z_set = None
for l1, l2 in combinations(lines, 2):
    if l1.v.x == l2.v.x and abs(l1.v.x) > 100:
        potential_x_set = calc_potential_set(l1.v.x, l1.p0.x, l2.v.x, l2.p0.x, potential_x_set)
    if l1.v.y == l2.v.y and abs(l1.v.y) > 100:
        potential_y_set = calc_potential_set(l1.v.y, l1.p0.y, l2.v.y, l2.p0.y, potential_y_set)
    if l1.v.z == l2.v.z and abs(l1.v.z) > 100:
        potential_z_set = calc_potential_set(l1.v.z, l1.p0.z, l2.v.z, l2.p0.z, potential_z_set)

assert(len(potential_x_set) == 1)
assert(len(potential_y_set) == 1)
assert(len(potential_z_set) == 1)
rock_v = Coord(potential_x_set.pop(), potential_y_set.pop(), potential_z_set.pop())

l1 = lines[0]
l2 = lines[1]
k1 = (l1.v.y - rock_v.y) / (l1.v.x - rock_v.x)
k2 = (l2.v.y - rock_v.y) / (l2.v.x - rock_v.x)
m1 = l1.p0.y - (k1 * l1.p0.x)
m2 = l2.p0.y - (k2 * l2.p0.x)
x = int((m2 - m1)/(k1 - k2))
y = int(k1 * x + m1)
t = (x - l1.p0.x) // (l1.v.x - rock_v.x)
z = l1.p0.z + (l1.v.z - rock_v.z) * t
print(x + y + z)