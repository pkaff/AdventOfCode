import numpy as np

file = open("input.txt", "r")
infections = file.readlines()
grid = np.chararray((2*2500+1, 2*2500+1))
grid[:] = b'.'
x = int(len(grid)/2)
y = int(len(grid)/2)
dirX = 0
dirY = -1
for k in range(len(infections)):
    infectionLine = infections[k].strip(' \n')
    halfLineLength = int(len(infectionLine)/2)
    grid[y-halfLineLength + k, x-halfLineLength:x+halfLineLength + 1] = list(infectionLine)
nInfections = 0
for i in range(10000000):
    if grid[y,x] == b'#':
        dirX, dirY = -dirY, dirX
        grid[y,x] = b'f'
    elif grid[y,x] == b'.':
        dirX, dirY = dirY, -dirX
        grid[y,x] = b'w'
    elif grid[y,x] == b'w':
        grid[y,x] = b'#'
        nInfections += 1
    elif grid[y,x] == b'f':
        dirX, dirY = -dirX, -dirY
        grid[y,x] = b'.'
    x += dirX
    y += dirY
print(nInfections)