from itertools import combinations
from sympy import Point, Segment, Polygon
coords = [Point(list(map(int, line.strip().split(',')))) for line in open("testinput.txt", "r").readlines()]
combs = combinations(coords, 2)
rects = [Polygon(p1, Point(p1.x, p2.y), p2, Point(p2.x, p1.y)) for p1, p2 in combs]
rects = sorted(rects, key=lambda rect: rect.area if isinstance(rect, Polygon) else 0, reverse=True)
borders = [Segment(p[0], p[1]) for p in zip(coords[:-1], coords[1:])] + [Segment(coords[-1], coords[0])]
for rect in rects:
    valid = True
    for border in borders:
        intersect = rect.intersection(border)
        assert(len(intersect) <= 1)
        if not intersect:
            continue
        ipoint = intersect[0]
        if isinstance(ipoint, Point) and (ipoint.x != border.p1.x or ipoint.y != border.p1.y) and (ipoint.x != border.p2.x or ipoint.y != border.p2.y):
            valid = False
            break
    if valid:
        print(rect.area)
        break