from copy import deepcopy

def inBounds(grid, y, x):
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y])

def findNeighbourSeats(grid, y, x):
    dirs = [(r, c) for r in range(-1, 2) for c in range(-1, 2) if r != 0 or c != 0]
    step = 1
    seats = {}
    anyDirInBounds = True
    while len(seats) != 8 and anyDirInBounds:
        anyDirInBounds = False
        for mydir in dirs:
            if mydir not in seats.keys():
                newY = y + mydir[0] * step
                newX = x + mydir[1] * step
                if inBounds(grid, newY, newX):
                    if grid[newY][newX] != '.':
                        seats[mydir] = grid[newY][newX]
                    anyDirInBounds = True
        step += 1
    return list(seats.values())

def getNextSeat(grid, y, x):
    if grid[y][x] == '.':
        return '.'
    seats = findNeighbourSeats(grid, y, x)
    occupied = seats.count('#')
    if grid[y][x] == 'L' and occupied == 0:
        return '#'
    if grid[y][x] == '#' and occupied >= 5:
        return 'L'
    return grid[y][x]

grid = [[c for c in l.rstrip("\n")] for l in open("input.txt", "r").readlines()]
while True:
    nextGrid = deepcopy(grid)
    changed = False
    for y in range(len(nextGrid)):
        for x in range(len(nextGrid[y])):
            nextGrid[y][x] = getNextSeat(grid, y, x)
            if nextGrid[y][x] != grid[y][x]:
                changed = True
    if not changed:
        print(sum([row.count('#') for row in nextGrid]))
        break
    grid = nextGrid