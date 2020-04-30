def canVisit(y, x):
    return (x >= 0 and x < len(maze[0]) and y >= 0 and y < len(maze) and maze[y][x] != ' ')
def nextDir(y, x, pYDir, pXDir):
    if pYDir != 0:
        yDirs = [0, 0];
        xDirs = [-1, 1];
    elif pXDir != 0:
        yDirs = [-1, 1];
        xDirs = [0, 0];
    for k in range(2):
        if canVisit(y + yDirs[k], x + xDirs[k]):
            return [yDirs[k], xDirs[k]]

file = open("input.txt", "r")
maze = file.readlines()
x = maze[0].index('|')
y = 0
xDir = 0
yDir = 1
steps = 0
while maze[y][x] != ' ':
    if maze[y][x] == '+':
        (yDir, xDir) = nextDir(y, x, yDir, xDir)
    x += xDir
    y += yDir
    steps += 1
print(steps)