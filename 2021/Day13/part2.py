from collections import defaultdict
myin, folds = open("input.txt", "r").read().split('\n\n')
points = set(tuple(map(int, point.split(','))) for point in myin.split('\n'))
folds = [(fold[fold.find('=') - 1], int(fold[fold.find('=') + 1:])) for fold in folds.split('\n') if fold]
def GetPosAfterFold(fold_pos, pos):
    if pos < fold_pos:
        return pos
    else:
        return fold_pos - (pos - fold_pos)
for direction, fold_pos in folds:
    if direction == 'x':
        points = set(map(lambda point: (GetPosAfterFold(fold_pos, point[0]), point[1]), points))
    elif direction == 'y':
        points = set(map(lambda point: (point[0], GetPosAfterFold(fold_pos, point[1])), points))
maxX = max(point[0] for point in points)
maxY = max(point[1] for point in points)
printstr = ''
for y in range(maxY + 1):
    for x in range(maxX + 1):
        if (x, y) in points:
            printstr += '#'
        else:
            printstr += '.'
    printstr += '\n'
print(printstr)
