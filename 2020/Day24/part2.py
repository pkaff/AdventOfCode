from functools import reduce
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

def countBlackNeighbours(coord, blackCoords):
    neighbours = getNeighbours(coord)
    return sum([1 for neighbour in neighbours if neighbour in blackCoords])

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
    if finalCoord in blackCoords:
        blackCoords.remove(finalCoord)
    else:
        blackCoords.add(finalCoord)

for day in range(100):
    coordsToCheck = set()
    for coord in blackCoords:
        coordsToCheck.add(coord)
        coordsToCheck.update(getNeighbours(coord))
    coordsToAdd = set()
    coordsToRemove = set()
    for coord in coordsToCheck:
        nBlack = countBlackNeighbours(coord, blackCoords)
        if coord in blackCoords and (nBlack == 0 or nBlack > 2):
            coordsToRemove.add(coord)
        elif coord not in blackCoords and nBlack == 2:
            coordsToAdd.add(coord)
    blackCoords |= coordsToAdd
    blackCoords -= coordsToRemove
print(len(blackCoords))