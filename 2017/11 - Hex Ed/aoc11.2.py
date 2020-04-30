file = open("input.txt", "r")
steps = file.read().split(",")
x = 0
y = 0
maxDist = 0
for s in steps:
    if s == 'sw':
        y -= 1
    if s == 'nw':
        x -= 1
    if s == 'n':
        x -= 1
        y += 1
    if s == 'ne':
        y += 1
    if s == 'se':
        x += 1
    if s == 's':
        x += 1
        y -= 1
    if (x < 0 and y < 0) or (x > 0 and y > 0):
        maxDist = max(maxDist, abs(x + y))
    else:
        maxDist = max(maxDist, max(abs(x), abs(y)))
print(maxDist)