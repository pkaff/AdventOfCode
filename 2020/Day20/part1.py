from collections import defaultdict
from collections import namedtuple
from collections import deque
from functools import reduce
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
print(reduce(lambda x, y: x * y, [int(tileId.rstrip(":").split()[1]) for tileId in cornerIds]))