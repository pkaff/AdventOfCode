from itertools import combinations
coords = [list(map(int, line.strip().split(','))) for line in open("input.txt", "r").readlines()]
combs = combinations(coords, 2)
def rect_size(x, y):
    maxx = max(x[0], y[0])
    maxy = max(x[1], y[1])
    minx = min(x[0], y[0])
    miny = min(x[1], y[1])
    return (maxx - minx + 1) * (maxy - miny + 1)
rect_sizes = sorted(combs, key=lambda pair: rect_size(pair[0], pair[1]), reverse=True)
print(rect_size(rect_sizes[0][0], rect_sizes[0][1]))