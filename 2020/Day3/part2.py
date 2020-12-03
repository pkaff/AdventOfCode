from functools import reduce
myin = [s.rstrip() for s in open("input.txt", "r").readlines()]
allTrees = []
for speedX, speedY in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
    posY = 0
    posX = 0
    trees = 0
    while posY < len(myin):
        if myin[posY][posX % len(myin[posY])] == '#':
            trees += 1
        posX += speedX
        posY += speedY
    allTrees.append(trees)
print(reduce(lambda x, y: x * y, allTrees))