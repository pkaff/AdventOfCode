from copy import deepcopy

def inBounds(grid, y, x):
    return y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y])

def getNextSeat(grid, y, x):
    if grid[y][x] == '.':
        return '.'
    occupied = 0
    for r in range(-1, 2):
        for c in range(-1, 2):
            if r != 0 or c != 0:
                if inBounds(grid, y + r, x + c):
                    if grid[y + r][x + c] == '#':
                        occupied += 1
    if grid[y][x] == 'L' and occupied == 0:
        return '#'
    if grid[y][x] == '#' and occupied >= 4:
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