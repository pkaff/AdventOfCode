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
    finalCoord = reduce(lambda c1, c2: (c1[0] + c2[0], c1[1] + c2[1], c1[2] + c2[2]), coordList)
    if finalCoord in blackCoords:
        blackCoords.remove(finalCoord)
    else:
        blackCoords.add(finalCoord)
print(len(blackCoords))
