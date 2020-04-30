from collections import defaultdict
import sys

turnSequence = ['L', 'S', 'R']
input = [[c for c in x.replace('\n', '')] for x in open("input.txt", "r").readlines()]
tracks = [[c for c in ''.join(l).replace('<', '-').replace('>', '-').replace('^', '|').replace('v', '|')] for l in input]
locToTurnIx = defaultdict(lambda: -1)
def getDir(c, dir, turnIx):
    if c == '<' or c == '>' or c == '^' or c == 'v':
        return 'x', turnIx
    if c == '\\':
        return '>' if dir == 'v' else '<' if dir == '^' else 'v' if dir == '>' else '^', turnIx
    elif c == '/':
        return '<' if dir == 'v' else '>' if dir == '^' else '^' if dir == '>' else 'v', turnIx
    elif c == '+':
        if turnSequence[turnIx] == 'L':
            return '>' if dir == 'v' else '<' if dir == '^' else '^' if dir == '>' else 'v', (turnIx + 1)%len(turnSequence)
        if turnSequence[turnIx] == 'S':
            return dir, (turnIx + 1)%len(turnSequence)
        if turnSequence[turnIx] == 'R':
            return '>' if dir == '^' else '<' if dir == 'v' else '^' if dir == '<' else 'v', (turnIx + 1)%len(turnSequence)
    else:
        return dir, turnIx
for y in range(0, len(input)):
    for x in range(0, len(input[y])):
        if input[y][x] == 'v' or '^' or '>' or '<':
            locToTurnIx[(x, y)] = 0
while True:
    hasMoved = defaultdict(lambda: False)
    for y in range(0, len(input)):
        for x in range(0, len(input[y])):
            curChar = input[y][x]
            if (curChar != 'v' and curChar != '^' and curChar != '>' and curChar != '<') or hasMoved[(x, y)]:
                continue
            #print(curChar) #should be cart
            nextY = y
            nextX = x
            if curChar == 'v':
                nextY += 1
            elif curChar == '^':
                nextY -= 1
                input[y][x] = '|'
            elif curChar == '>':
                nextX += 1
            elif curChar == '<':
                nextX -= 1
            else:
                print('Not cart')
                sys.exit()
            input[nextY][nextX], locToTurnIx[(nextX, nextY)] = getDir(input[nextY][nextX], curChar, locToTurnIx[(x, y)])
            locToTurnIx[(x, y)] = -1
            #print('pushing cart', curChar, 'from', x, y, 'to', nextX, nextY, 'turnix', locToTurnIx[(x, y)])
            input[y][x] = tracks[y][x]
            if input[nextY][nextX] == 'x':
                print(nextX, nextY)
                sys.exit()
            hasMoved[(nextX, nextY)] = True
    #for i in input:
    #    print(''.join(i))