from functools import reduce
from collections import defaultdict
def dirToCoord(mydir):
    if mydir == 'se':
        return (0, -1, 1)
    elif mydir == 'sw':
        return (-1, 0, 1)
    elif mydir == 'w':
        return (-1, 1, 0)
    elif mydir == 'nw':
        return (0, 1, -1)
    elif mydir == 'ne':
        return (1, 0, -1)
    else:
        return (1, -1, 0)

def addCoords(c1, c2):
    return (c1[0] + c2[0], c1[1] + c2[1], c1[2] + c2[2])

def getNeighbours(coord):
    neighbourDirs = [(1, -1, 0), (1, 0, -1), (0, 1, -1), (-1, 1, 0), (-1, 0, 1), (0, -1, 1)]
    return [addCoords(coord, neighbourDir) for neighbourDir in neighbourDirs]

def countBlackNeighbours(coord, flippedCoords):
    neighbours = getNeighbours(coord)
    return sum([1 for neighbour in neighbours if flippedCoords[neighbour]])

def calculateWhiteTilesToFlip(flippedCoords):
    maxX = max(flippedCoords, key = lambda i : i[0])[0]
    maxY = max(flippedCoords, key = lambda i : i[1])[1]
    maxZ = max(flippedCoords, key = lambda i : i[2])[2]
    minX = min(flippedCoords, key = lambda i : i[0])[0]
    minY = min(flippedCoords, key = lambda i : i[1])[1]
    minZ = min(flippedCoords, key = lambda i : i[2])[2]
    toFlip = []
    for x in range(minX - 1, maxX + 2):
        for y in range(minY - 1, maxY + 2):
            for z in range(minZ - 1, maxZ + 2):
                coord = (x, y, z)
                if not flippedCoords[coord]:
                    nBlackNeighbours = countBlackNeighbours(coord, flippedCoords)
                    if nBlackNeighbours == 2:
                        toFlip.append(coord)
    return toFlip

myinput = [l.rstrip() for l in open("input.txt").readlines()]
blackCoords = set()
for line in myinput:
    ix = 0
    coordList = []
    while ix < len(line):
        if line[ix] == 's' or line[ix] == 'n':
            coordList.append(dirToCoord(line[ix : ix + 2]))
            ix += 2
        else:
            coordList.append(dirToCoord(line[ix]))
            ix += 1
    finalCoord = reduce(addCoords, coordList)
    blackCoords.add(finalCoord)

for day in range(100):
    tilesToFlip = calculateWhiteTilesToFlip(flippedCoords)
    newFlippedCoords = flippedCoords.copy()
    for tile in tilesToFlip:
        newFlippedCoords[tile] = True
    for kv in flippedCoords.items():
        if kv[1]:
            blackCoord = kv[0]
            nBlackNeighbours = countBlackNeighbours(blackCoord, flippedCoords)
            if nBlackNeighbours == 0 or nBlackNeighbours > 2:
                newFlippedCoords[blackCoord] = False
print(sum([1 for val in flippedCoords.values() if val]))