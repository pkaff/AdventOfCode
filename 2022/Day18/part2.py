from collections import defaultdict

def get_neighbours(x, y, z):
    neighbours = []
    for diff in [-1, 1]:
        neighbours.append((x + diff, y, z))
        neighbours.append((x, y + diff, z))
        neighbours.append((x, y, z + diff))
    return neighbours

def get_connected_group(x, y, z, visited, group):
    group.append((x, y, z))
    visited.add((x, y, z))

    if x == minX or x == maxX or y == minY or y == maxY or z == maxZ or z == minZ:
        return False, group

    neighbours = get_neighbours(x, y, z)

    for neighbour in neighbours:
        if neighbour not in visited and not input[neighbour]:
            contained, group = get_connected_group(*neighbour, visited, group)
            if not contained:
                return False, group

    return True, group

def count_sides(group):
    sides = len(group) * 6
    for x, y, z in group:
        neighbours = get_neighbours(x, y, z)
        for neighbour in neighbours:
            if neighbour in group:
                sides -= 1
    return sides

input = defaultdict(bool)
for line in open("input.txt", "r").readlines():
    input[tuple(map(int, line.strip('\n').split(',')))] = True

num_exposed_sides = len(input) * 6
for x, y, z in input.keys():
    neighbours = get_neighbours(x, y, z)
    for neighbour in neighbours:
        if neighbour in input:
            num_exposed_sides -= 1

maxX = max([coord[0] for coord in input.keys()])
minX = min([coord[0] for coord in input.keys()])
maxY = max([coord[1] for coord in input.keys()])
minY = min([coord[1] for coord in input.keys()])
maxZ = max([coord[2] for coord in input.keys()])
minZ = min([coord[2] for coord in input.keys()])

visited = set()
for x in range(minX + 1, maxX):
    for y in range(minY + 1, maxY):
        for z in range(minZ + 1, maxZ):
            if not input[(x, y, z)] and (x, y, z) not in visited:
                was_contained, connected = get_connected_group(x, y, z, set(), [])
                if was_contained:
                    visited.update(connected)
                    num_exposed_sides -= count_sides(connected)
print(num_exposed_sides)