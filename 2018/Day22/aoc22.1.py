depth = 3198
tx, ty = (12,757)
   
cave = [[None for x in range(tx + 1)] for y in range(ty + 1)]
cave[0][0] = 0
cave[ty][tx] = 0

def erosionLevel(x, y):
    if cave[y][x] is not None:
        return cave[y][x]
    gIx = None
    if x == 0:
        gIx = y * 48271
    elif y == 0:
        gIx = x * 16807
    else:
        gIx = erosionLevel(x - 1, y) * erosionLevel(x, y - 1)
    cave[y][x] = (gIx + depth) % 20183
    return cave[y][x]

def riskLevel(x, y):
    return erosionLevel(x, y) % 3

print(sum(erosionLevel(x, y) % 3 for x in range(tx + 1) for y in range(ty + 1)))
