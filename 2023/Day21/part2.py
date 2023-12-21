input = open("input.txt", "r").readlines()
blocked = {(x, y): c for y, row in enumerate(input) for x, c in enumerate(row.strip()) if c == '#' or c == 'S'}
start = list(blocked.keys())[list(blocked.values()).index('S')]
blocked.pop(start)
width = len(input)
height = len(input[0].strip())

def get_neighbours(x, y):
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    return [(x + dx, y + dy) for dx, dy in dirs]

steps = 26501365
to_visit = {start}
a_is = []
for ix in range(1, 1000000):
    next_visit = set()
    for x, y in to_visit:
        for nx, ny in get_neighbours(x, y):
            if (nx % width, ny % height) not in blocked:
                next_visit.add((nx, ny))
    to_visit = next_visit
    if ix % width == steps % width:
        a_is.append(len(to_visit))
        print(a_is)
        if len(a_is) == 3:
            break

# quadratic interpolation
def f(n, a0, a1, a2):
    b0 = a0
    b1 = a1-a0
    b2 = a2-a1
    return b0 + b1*n + (n*(n-1)//2)*(b2-b1)
print(f(steps//width, *a_is))