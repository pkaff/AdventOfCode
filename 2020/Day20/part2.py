from collections import defaultdict
from collections import namedtuple
from collections import deque
from collections import Counter
from math import sqrt
import numpy as np
def getRotMirrors(img):
    res = []
    originalArr = np.array([[c for c in row] for row in img])
    for rotation in range(4):
        if rotation != 0:
            rotatedArr = np.rot90(originalArr, rotation)
        else:
            rotatedArr = originalArr
        for mirror in range(2):
            if mirror == 1:
                mirroredArr = np.fliplr(rotatedArr)
            else:
                mirroredArr = rotatedArr
            res.append((mirroredArr, rotation, mirror))
    return res

def getRotatedMirrored(img, rotation, mirror):
    originalArr = np.array([[c for c in row] for row in img])
    if rotation != 0:
        rotatedArr = np.rot90(originalArr, rotation)
    else:
        rotatedArr = originalArr
    if mirror == 1:
        mirroredArr = np.fliplr(rotatedArr)
    else:
        mirroredArr = rotatedArr
    return mirroredArr

def getSeaMonsterCoords(x, y):
    l1 = [pos for pos, char in enumerate("                  # ") if char == "#"]
    l2 = [pos for pos, char in enumerate("#    ##    ##    ###") if char == "#"]
    l3 = [pos for pos, char in enumerate(" #  #  #  #  #  #   ") if char == "#"]
    coords = []
    for dx in l1:
        coords.append((x + dx, y))
    for dx in l2:
        coords.append((x + dx, y + 1))
    for dx in l3:
        coords.append((x + dx, y + 2))
    return coords

def nSeaMonsters(finalImage):
    seaMonsterLen = 20
    seaMonsterHeight = 3
    nSeaMonsters = 0
    for x in range(imageSize*gridSize - seaMonsterLen + 1):
        for y in range(imageSize*gridSize - seaMonsterHeight + 1):
            coords = getSeaMonsterCoords(x, y)
            if all([finalImage[yy][xx] == '#' for xx, yy in coords]):
                nSeaMonsters += 1
    return nSeaMonsters

TileIdentifier = namedtuple("TileIdentifier", "tileId, rotation, mirror")
images = open("input.txt", "r").read().split("\n\n")
images = {img.split("\n")[0]: img.split("\n")[1:] for img in images}
topBorders = defaultdict(list)
leftBorders = defaultdict(list)
rightBorders = defaultdict(list)
bottomBorders = defaultdict(list)
for tileId, img in images.items():
    for rotMirroredArr, rotation, mirror in getRotMirrors(img):
        topBorder = "".join(rotMirroredArr[0])
        leftBorder = "".join([row[0] for row in rotMirroredArr])
        rightBorder = "".join([row[-1] for row in rotMirroredArr])
        bottomBorder = "".join(rotMirroredArr[-1])
        topBorders[topBorder].append(TileIdentifier(tileId, rotation, mirror))
        leftBorders[leftBorder].append(TileIdentifier(tileId, rotation, mirror))
        rightBorders[rightBorder].append(TileIdentifier(tileId, rotation, mirror))
        bottomBorders[bottomBorder].append(TileIdentifier(tileId, rotation, mirror))

toVisit = deque()
toVisit.append(TileIdentifier("Tile 2473:", 0, 0))
cornerIds = []
visited = []
topLeftCorner = None
while toVisit:
    tileId, rotation, mirror = toVisit.pop()
    if tileId not in visited:
        visited.append(tileId)
        rotMirroredArr = getRotatedMirrored(images[tileId], rotation, mirror)
        topBorder = "".join(rotMirroredArr[0])
        leftBorder = "".join([row[0] for row in rotMirroredArr])
        rightBorder = "".join([row[-1] for row in rotMirroredArr])
        bottomBorder = "".join(rotMirroredArr[-1])
        matchingBottom = [tileIdentifier for tileIdentifier in topBorders[bottomBorder] if tileIdentifier.tileId != tileId]
        for nextTile in matchingBottom:
            if nextTile.tileId not in visited:
                toVisit.append(nextTile)
        matchingLeft = [tileIdentifier for tileIdentifier in rightBorders[leftBorder] if tileIdentifier.tileId != tileId]
        for nextTile in matchingLeft:
            if nextTile.tileId not in visited:
                toVisit.append(nextTile)
        matchingRight = [tileIdentifier for tileIdentifier in leftBorders[rightBorder] if tileIdentifier.tileId != tileId]
        for nextTile in matchingRight:
            if nextTile.tileId not in visited:
                toVisit.append(nextTile)
        matchingTop = [tileIdentifier for tileIdentifier in bottomBorders[topBorder] if tileIdentifier.tileId != tileId]
        for nextTile in matchingTop:
            if nextTile.tileId not in visited:
                toVisit.append(nextTile)
        if tileId not in cornerIds and ((not matchingBottom and not matchingLeft) or (not matchingBottom and not matchingRight) or (not matchingTop and not matchingLeft) or (not matchingTop and not matchingRight)):
            cornerIds.append(tileId)
            if not matchingTop and not matchingLeft:
                topLeftCorner = TileIdentifier(tileId, rotation, mirror)
gridSize = int(sqrt(len(images)))
imageSize = len(images["Tile 2473:"]) - 2
finalImage = [None]*imageSize*gridSize
for i in range(imageSize*gridSize):
    finalImage[i] = [None] * imageSize*gridSize
toVisit = deque()
toVisit.append(topLeftCorner)
visited = []
xPos = 0
yPos = 0
while toVisit:
    tileId, rotation, mirror = toVisit.pop()
    if tileId not in visited:
        visited.append(tileId)
        rotMirroredArr = getRotatedMirrored(images[tileId], rotation, mirror)
        topBorder = "".join(rotMirroredArr[0])
        leftBorder = "".join([row[0] for row in rotMirroredArr])
        rightBorder = "".join([row[-1] for row in rotMirroredArr])
        bottomBorder = "".join(rotMirroredArr[-1])
        matchingRight = [tileIdentifier for tileIdentifier in leftBorders[rightBorder] if tileIdentifier.tileId != tileId]
        for nextTile in matchingRight:
            if nextTile.tileId not in visited:
                toVisit.append(nextTile)
        matchingBottom = [tileIdentifier for tileIdentifier in topBorders[bottomBorder] if tileIdentifier.tileId != tileId]
        for nextTile in matchingBottom:
            if nextTile.tileId not in visited:
                toVisit.appendleft(nextTile)
        y = yPos * imageSize
        for row in ["".join(line) for line in rotMirroredArr[1:-1, 1:-1]]:
            x = xPos * imageSize
            for c in row:
                finalImage[y][x] = c
                x += 1
            y += 1
        xPos = int((xPos + 1) % gridSize)
        yPos += int(xPos == 0)

for rotMirrors in getRotMirrors(finalImage):
    image = rotMirrors[0]
    nMonsters = nSeaMonsters(image)
    if nMonsters > 0:
        seaMonsterSize = len(getSeaMonsterCoords(0, 0))
        print(sum([Counter(row)['#'] for row in image]) - seaMonsterSize * nMonsters)
