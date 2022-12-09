import math
def dist(head, tail):
    return max(abs(head[0] - tail[0]), abs(head[1] - tail[1]))
def get_steps(head, tail):
    ret = []
    while dist(head, tail) > 1:
        stepx = int(math.copysign(1, head[0] - tail[0]))
        stepy = int(math.copysign(1, head[1] - tail[1]))
        if head[0] == tail[0]:
            stepx = 0
        if head[1] == tail[1]:
            stepy = 0
        ret.append((stepx, stepy))
        tail = (tail[0] + stepx, tail[1] + stepy)
    return ret
movements = [[pair[0], int(pair[1])] for pair in [line.strip().split() for line in open("input.txt", "r").readlines()]]
x = 0
y = 0
head_pos = (x, y)
tail_pos = (x, y)
visited = dict()
visited[tail_pos] = True
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
    head_pos = (head_pos[0] + dx * step, head_pos[1] + dy * step)
    for stepx, stepy in get_steps(head_pos, tail_pos):
        tail_pos = (tail_pos[0] + stepx, tail_pos[1] + stepy)
        visited[tail_pos] = True

print(sum(1 for _ in visited.values()))
