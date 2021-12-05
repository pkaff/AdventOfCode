from collections import defaultdict
myin = [[list(map(int, coords.split(','))) for coords in line.replace('\n', '').split(' -> ')] for line in open("input.txt", "r").readlines()]
covered_coords = defaultdict(int)
for (x1, y1), (x2, y2) in myin:
    ytmp = y1
    xtmp = x1
    ydir = 1 if y2 > y1 else -1 if y2 < y1 else 0
    xdir = 1 if x2 > x1 else -1 if x2 < x1 else 0
    while (ytmp - y2) != 0 or (xtmp - x2) != 0:
        covered_coords[(xtmp, ytmp)] += 1
        xtmp += xdir
        ytmp += ydir
    covered_coords[(xtmp, ytmp)] += 1
print(sum(value >= 2 for value in covered_coords.values()))