import math
def dist(head, tail):
    return max(abs(head[0] - tail[0]), abs(head[1] - tail[1]))
def update_tail(head, tails, visited):
    for ix, tail in enumerate(tails):
        if dist(head, tail) > 1:
            stepx = int(math.copysign(1, head[0] - tail[0]))
            stepy = int(math.copysign(1, head[1] - tail[1]))
            if head[0] == tail[0]:
                stepx = 0
            if head[1] == tail[1]:
                stepy = 0
            tail[0] += stepx
            tail[1] += stepy
            head = tail
            if ix == len(tails) - 1:
                visited[tuple(tail)] = True
        else:
            break
def print_knot(head, tails):
    printstr = ""
    for y in range(30):
        for x in range(30):
            printed = False
            if head[0] == x and head[1] == y:
                printstr += 'H'
                printed = True
            else:
                for ix, tail in enumerate(tails):
                    if tail[0] == x and tail[1] == y:
                        printstr += str(ix + 1)
                        printed = True
                        break
            if not printed:
                printstr += '.'
        printstr += '\n'
    print(printstr)
movements = [[pair[0], int(pair[1])] for pair in [line.strip().split() for line in open("input.txt", "r").readlines()]]
x = 0
y = 0
head_pos = [x, y]
tail_poss = [[x, y] for _ in range(9)]
visited = dict()
visited[tuple(tail_poss[-1])] = True
for dir, step in movements:
    dx = 0
    dy =  0
    if dir == 'U':
        dy = 1
    if dir == 'D':
        dy = -1
    if dir == 'R':
        dx = 1
    if dir == 'L':
        dx = -1
    for _ in range(step):
        head_pos[0] += dx
        head_pos[1] += dy
        update_tail(head_pos, tail_poss, visited)

print(sum(1 for _ in visited.values()))
