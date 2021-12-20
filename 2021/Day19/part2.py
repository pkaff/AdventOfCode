from itertools import permutations
scanners = [[tuple(map(int, coords.split(','))) for coords in scanner.split('\n')[1:] if coords] for scanner in open("input.txt", "r").read().split('\n\n')]

def get_2drotations(x, y, z):
    return [(x, y, z), (x, -z, y), (x, -y, -z), (x, z, -y)]

def get_axis_combinations(x, y, z):
    return [(x, y, z), (-x, y, -z), (y, -x, z), (-y, x, z), (z, y, -x), (-z, y, x)]

def get_rotations(coord):
    (x, y, z) = coord
    rotated_coords = []
    for (xx, yy, zz) in get_axis_combinations(x, y, z):
        rotated_coords += get_2drotations(xx, yy, zz)
    return rotated_coords

def get_list_rotations(coords):
    all_rotations = [[] for _ in range(24)]
    for cix, coord in enumerate(coords):
        rotations = get_rotations(coord)
        for rix, rotation in enumerate(rotations):
            all_rotations[rix].append(rotation)

    return all_rotations

def coord_in_scanner(fixed_coords, coord):
    (x, y, z) = coord
    for (fx, fy, fz) in fixed_coords:
        dx, dy, dz = (fx - x, fy - y, fz - z)
        s = {x + dx, y + dy, z + dz}

def match(fixed_scanners, coords):
    for _, fixed_coords in fixed_scanners:
        for (fx, fy, fz) in fixed_coords:
            for (x, y, z) in coords:
                dx, dy, dz = (fx - x, fy - y, fz - z)
                shifted_coords = set((x + dx, y + dy, z + dz) for x, y, z in coords)
                if len(shifted_coords & fixed_coords) >= 12:
                    return True, shifted_coords, (dx, dy, dz)
    return False, set(), None

def manhattan_dist(a, b):
    x, y, z = a
    xx, yy, zz = b
    return abs(x - xx) + abs(y - yy) + abs(z - zz)

fixed_scanners = [((0, 0, 0), set(scanners[0]))]
relative_scanners = scanners[1:]
ix = 0
while True:
    relative_coords = relative_scanners[ix]
    for rotated_coords in get_list_rotations(relative_coords):
        matched, shifted_coords, fixed_pos = match(fixed_scanners, rotated_coords)
        if matched:
            fixed_scanners.append((fixed_pos, shifted_coords))
            relative_scanners.pop(ix)
    if len(relative_scanners) == 0:
        break
    ix = (ix + 1) % len(relative_scanners)
print(max([manhattan_dist(first, second) for first, second in permutations([pos for pos, _ in fixed_scanners], 2)]))