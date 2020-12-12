def rotate(cmd, val, wpX, wpY):
    nRotations = int(val / 90)
    for rot in range(nRotations):
        oldWpX = wpX
        oldWpY = wpY
        if cmd == 'L':
            wpX = -oldWpY
            wpY = oldWpX
        elif cmd == 'R':
            wpX = oldWpY
            wpY = -oldWpX
    return wpX, wpY

myinput = [(l[0], int(l.rstrip("\n")[1:])) for l in open("input.txt", "r").readlines()]
x = 0
y = 0
wpX = 10
wpY = 1
for cmd, val in myinput:
    if cmd == 'N':
        wpY += val
    elif cmd == 'S':
        wpY -= val
    elif cmd == 'E':
        wpX += val
    elif cmd == 'W':
        wpX -= val
    elif cmd == 'L' or cmd == 'R':
        wpX, wpY = rotate(cmd, val, wpX, wpY)
    elif cmd == 'F':
        x += wpX * val
        y += wpY * val
print(abs(x) + abs(y))