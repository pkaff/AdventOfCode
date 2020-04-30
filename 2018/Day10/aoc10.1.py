from collections import defaultdict
from matplotlib import pyplot as plt
import re

fig = plt.figure()
ax = plt.axes(xlim=(-500, 500), ylim=(-500, 500))
line, = ax.plot([], [], 'x')

input = [re.findall(r'(\<-?\d+,-?\d+\>)', x.replace(' ', '')) for x in open("input.txt", "r").readlines()]
coordinates = [list(map(int, x[0].replace('<', '').replace('>', '').split(','))) for x in input]
velocities = [list(map(int, x[1].replace('<', '').replace('>', '').split(','))) for x in input]

minAreaIx = 0
minArea = 10000
for i in range(20000):
    minX = 50000
    minY = 50000
    maxX = -50000
    maxY = -50000
    for ix in range(0, len(input)):
        minX = min(coordinates[ix][0] + i * velocities[ix][0], minX)
        maxX = max(coordinates[ix][0] + i * velocities[ix][0], maxX)
        minY = min(coordinates[ix][1] + i * velocities[ix][1], minY)
        maxY = max(coordinates[ix][1] + i * velocities[ix][1], maxY)
    if maxX - minX + maxY - minY < minArea:
        minAreaIx = i
        minArea = maxX - minX + maxY - minY
print(minAreaIx)
for vx in range(0, len(velocities)):
    coordinates[vx][0] += minAreaIx*velocities[vx][0]
    coordinates[vx][1] += minAreaIx*velocities[vx][1]
x, y = zip(*coordinates)
plt.scatter(x, y)
plt.show()
