print([line[(posY * 3) % len(line)] for posY, line in enumerate([s.rstrip() for s in open("input.txt", "r").readlines()])].count('#'))

myin = [s.rstrip() for s in open("input.txt", "r").readlines()]
posY = 0
posX = 0
trees = 0
while posY < len(myin):
    if myin[posY][posX % len(myin[posY])] == '#':
        trees += 1
    posX += 3
    posY += 1
print(trees)
