from collections import defaultdict
import numpy as np

grid = np.zeros((301, 301), dtype=int) #y,x
sNo = 7989

for x in range(1, grid.shape[1]):
    for y in range(1, grid.shape[0]):
        rackID = x + 10
        pwrLvl = rackID * y
        pwrLvl += sNo
        pwrLvl *= rackID
        pwrLvl = (pwrLvl//100)%10
        pwrLvl -= 5
        grid[y,x] = pwrLvl
maxSize = 0
bestCoord = ()
for sqSize in range(1, 301):
    for y in range(1, grid.shape[0] - sqSize + 1):
        for x in range(1, grid.shape[1] - sqSize + 1):
            curSq = grid[y:y+sqSize,x:x+sqSize]
            if curSq.sum() > maxSize:
                bestCoord = (x, y, sqSize)
                maxSize = max(maxSize, curSq.sum())
print(bestCoord)
