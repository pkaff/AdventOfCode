def canVisit(y, x):
    return (x >= 0 and x < len(maze[0]) and y >= 0 and y < len(maze) and maze[y][x] != ' ')
def nextDir(y, x, pYDir, pXDir):
    print(y, x)
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
lettersFound = []
while maze[y][x] != ' ':
    if maze[y][x] == '+':
        (yDir, xDir) = nextDir(y, x, yDir, xDir)
    elif maze[y][x] != '-' and maze[y][x] != '|':
        lettersFound.append(maze[y][x])
    x += xDir
    y += yDir
print(''.join(lettersFound))