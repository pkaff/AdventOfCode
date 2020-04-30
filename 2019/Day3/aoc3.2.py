import sys
def appendCoords(x, y, str, coords, steps):
    dir = str[0]
    cordLen = int(str[1:])
    for _ in range(cordLen):
        steps += 1
        if dir == 'U':
            y += 1
        if dir == 'D':
            y -= 1
        if dir == 'R':
            x += 1
        if dir == 'L':
            x -= 1
        coords[x, y] = steps
    return (x, y, steps)
cord1, cord2 = [x.strip().split(",") for x in open("input.txt", "r").readlines()]
x = 0
y = 0
steps = 0
coords1 = {}
coords2 = {}
for str1 in cord1:
    x, y, steps = appendCoords(x, y, str1, coords1, steps)
x = 0
y = 0
steps = 0
for str2 in cord2:
    x, y, steps = appendCoords(x, y, str2, coords2, steps)
minSteps = sys.maxint
intersections = set(coords1) & set(coords2)
for p in intersections:
    dist = coords1[p] + coords2[p]
    minSteps = min(minSteps, dist)
print(minSteps)
