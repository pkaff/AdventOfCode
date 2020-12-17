def calculateNeighbours(x, y, z):
    return [(xx, yy, zz) for xx in range(x - 1, x + 2) for yy in range(y - 1, y + 2) for zz in range(z - 1, z + 2) if (xx != x or yy != y or zz != z)]
def countActiveNeighbours(actives, point):
    neighbours = calculateNeighbours(point[0], point[1], point[2])
    nActive = 0
    for neighbour in neighbours:
        if neighbour in actives:
            nActive += 1
    return nActive
def calculateNewActives(actives):
    maxX = max(actives, key = lambda i : i[0])[0]
    maxY = max(actives, key = lambda i : i[1])[1]
    maxZ = max(actives, key = lambda i : i[2])[2]
    minX = min(actives, key = lambda i : i[0])[0]
    minY = min(actives, key = lambda i : i[1])[1]
    minZ = min(actives, key = lambda i : i[2])[2]
    newActives = []
    for x in range(minX - 1, maxX + 2):
        for y in range(minY - 1, maxY + 2):
            for z in range(minZ - 1, maxZ + 2):
                point = (x, y, z)
                if point not in actives:
                    if countActiveNeighbours(actives, point) == 3:
                        newActives.append(point)
    return newActives
actives = [(x, y, 0) for y, l in enumerate(open("input.txt", "r").readlines()) for x, c in enumerate(l) if c == '#']
for cycle in range(6):
    nextActive = actives[:]
    for active in actives:
        nActive = countActiveNeighbours(actives, active)
        if not (nActive == 2 or nActive == 3):
            nextActive.remove(active)
    nextActive +=  calculateNewActives(actives)
    actives = nextActive
print(len(nextActive))


