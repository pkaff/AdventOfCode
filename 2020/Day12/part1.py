myinput = [(l[0], int(l.rstrip("\n")[1:])) for l in open("input.txt", "r").readlines()]
dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
curDirIx = 0
x = 0
y = 0
for cmd, val in myinput:
    curDir = dirs[int(curDirIx)]
    if cmd == 'N':
        y += val
    elif cmd == 'S':
        y -= val
    elif cmd == 'E':
        x += val
    elif cmd == 'W':
        x -= val
    elif cmd == 'L':
        curDirIx = (curDirIx + (val / 90)) % len(dirs)
    elif cmd == 'R':
        curDirIx = (curDirIx - (val / 90)) % len(dirs)
    elif cmd == 'F':
        x += curDir[0] * val
        y += curDir[1] * val
print(abs(x) + abs(y))