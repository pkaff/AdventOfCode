import sys
def appendCoords(x, y, str, coords):
    dir = str[0]
    cordLen = int(str[1:])
    for _ in range(cordLen):        
        if dir == 'U':
            y += 1
        if dir == 'D':
            y -= 1
        if dir == 'R':
            x += 1
        if dir == 'L':
            x -= 1
        coords.append((x, y))
    return (x, y)
def manhattan(x, y):
    return abs(x) + abs(y)
cord1, cord2 = [x.strip().split(",") for x in open("input.txt", "r").readlines()]
x = 0
y = 0
coords1 = []
coords2 = []
for str1 in cord1:
    x, y, = appendCoords(x, y, str1, coords1)
x = 0
y = 0
for str2 in cord2:
    x, y = appendCoords(x, y, str2, coords2)
minDist = sys.maxint
intersections = set(coords1) & set(coords2)
for p in intersections:
    dist = manhattan(p[0], p[1])
    minDist = min(minDist, dist)
print(minDist)
