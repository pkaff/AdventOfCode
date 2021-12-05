from collections import defaultdict
myin = [[list(map(int, coords.split(','))) for coords in line.replace('\n', '').split(' -> ')] for line in open("input.txt", "r").readlines()]
covered_coords = defaultdict(int)
for (x1, y1), (x2, y2) in myin:
    if y1 == y2:
        xtmp = min(x1, x2)
        while xtmp <= max(x1, x2):
            covered_coords[(xtmp, y1)] += 1
            xtmp += 1
    elif x1 == x2:
        ytmp = min(y1, y2)
        while ytmp <= max(y1, y2):
            covered_coords[(x1, ytmp)] += 1
            ytmp += 1
print(sum(value >= 2 for value in covered_coords.values()))