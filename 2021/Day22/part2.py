from functools import reduce

reboot_steps = [line.split() for line in open("input.txt", "r").read().split('\n') if line]
for ix, kv in enumerate(reboot_steps):
    coords = [list(map(int, coord.replace('x=', '').replace('y=', '').replace('z=', '').split('..'))) for coord in kv[1].split(',')]
    reboot_steps[ix] = (kv[0], coords)

def get_overlap(r1, r2):
    if r2[0] > r1[1] or r1[0] > r2[1]:
        return None
    return [max(r1[0], r2[0]), min(r1[1], r2[1])]

def split_active_cuboid(active_cuboid, new_cuboid):
    xa, ya, za = active_cuboid
    xn, yn, zn = new_cuboid

    xinter = get_overlap(xa, xn)
    yinter = get_overlap(ya, yn)
    zinter = get_overlap(za, zn)

    if not all([xinter, yinter, zinter]):
        return [active_cuboid]

    active_cuboid_split = []
    active_cuboid_split.append([xa, ya, [za[0], zinter[0] - 1]])
    active_cuboid_split.append([xa, ya, [zinter[1] + 1, za[1]]])
    active_cuboid_split.append([[xa[0], xinter[0] - 1], ya, zinter])
    active_cuboid_split.append([[xinter[1] + 1, xa[1]], ya, zinter])
    active_cuboid_split.append([xinter, [ya[0], yinter[0] - 1], zinter])
    active_cuboid_split.append([xinter, [yinter[1] + 1, ya[1]], zinter])

    return [(x, y, z) for x, y, z in active_cuboid_split if x[0] <= x[1] and y[0] <= y[1] and z[0] <= z[1]]

active_cuboids = []
for mode, cuboid in reboot_steps:
    new_cuboids = []
    for active_cuboid in active_cuboids:
        new_cuboids.extend(split_active_cuboid(active_cuboid, cuboid))
    if mode == 'on':
        new_cuboids.append(cuboid)
    active_cuboids = new_cuboids

n_active = 0
for cuboid in active_cuboids:
    n_active += reduce(lambda a, b: a * b, [(cuboid[i][1] - cuboid[i][0] + 1) for i in range(3)])
print(n_active)
