from itertools import combinations, pairwise
coords = [list(map(int, line.strip().split(','))) for line in open("input.txt", "r").readlines()]
def sorted_boundaries(boundaries):
    return [(min(p1[0], p2[0]), min(p1[1], p2[1]), max(p1[0], p2[0]), max(p1[1], p2[1])) for p1, p2 in boundaries]
combs = sorted_boundaries(combinations(coords, 2))
borders = sorted_boundaries(pairwise(coords))
maxSize = 0
for minx, miny, maxx, maxy in combs:
    size = (maxx - minx + 1) * (maxy - miny + 1)
    if size > maxSize:
        valid = True
        for bminx, bminy, bmaxx, bmaxy in borders:
            if bminx < maxx and bminy < maxy and bmaxx > minx and bmaxy > miny:
                valid = False
        if valid:
            maxSize = size
print(maxSize)
