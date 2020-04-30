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

sqSize = 3
sqSizes = defaultdict(int)
for x in range(1, grid.shape[1] - sqSize + 1):
	for y in range(1, grid.shape[0] - sqSize + 1):
		for xx in range(0, sqSize):
			for yy in range(0, sqSize):
				sqSizes[(x, y)] += grid[y + yy, x + xx]
print(max(sqSizes.keys(), key=lambda key: sqSizes[key]))
