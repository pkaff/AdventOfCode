from collections import defaultdict
def get_neighbours(x, y, z):
    neighbours = []
    for diff in [-1, 1]:
        neighbours.append((x + diff, y, z))
        neighbours.append((x, y + diff, z))
        neighbours.append((x, y, z + diff))
    return neighbours
input = defaultdict(bool)
input = {tuple(map(int, line.strip('\n').split(','))): True for line in open("input.txt", "r").readlines()}
num_exposed_sides = len(input) * 6
for x, y, z in input.keys():
    neighbours = get_neighbours(x, y, z)
    for neighbour in neighbours:
        if neighbour in input:
            num_exposed_sides -= 1
print(num_exposed_sides)

