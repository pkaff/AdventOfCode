import heapq

depth = 3198
tx, ty = (12,757)
   
cave = [[None for x in range(1000)] for y in range(1000)]
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

queue = [(0, 0, 0, 1)] #time, x, y, torch = 1, neither = 0, cg = 2
best = dict()
target = (tx, ty, 1)
while queue:
    time, x, y, tool = heapq.heappop(queue)
    bestKey = (x, y, tool)
    if bestKey in best and best[bestKey] <= time:
        continue
    best[bestKey] = time

    if bestKey == target:
        print(time)
        break
    
    for t in range(3):
        if t != tool and t != riskLevel(x, y):
            heapq.heappush(queue, (time + 7, x, y, t))
    
    for (xx, yy) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if x + xx < 0 or y + yy < 0:
            continue
        if riskLevel(x + xx, y + yy) == tool:
            continue
        heapq.heappush(queue, (time + 1, x + xx, y + yy, tool))