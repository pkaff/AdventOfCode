instructions = [(row.split()[0], int(row.split()[1])) for row in open("input.txt", "r").readlines()]
instructions = [(complex(dir.replace('R', '1').replace('L','-1').replace('U','-1j').replace('D','1j')), steps) for dir, steps in instructions]
border = set()
start = 0j
border.add(start)
for dir, steps in instructions:
    diff = dir * steps
    end = start + diff
    dx = 1 if diff.real > 0 else -1
    dy = 1 if diff.imag > 0 else -1
    border |= set({complex(x, y) for x in range(int(start.real), int(end.real) + dx, dx) for y in range(int(start.imag), int(end.imag) + dy, dy)})
    start = end

max_x = int(max(border, key=lambda c: c.real).real)
max_y = int(max(border, key=lambda c: c.imag).imag)
min_x = int(min(border, key=lambda c: c.real).real)
min_y = int(min(border, key=lambda c: c.imag).imag)

r_corners = set()
l_corners = set()
for x in range(min_x, max_x + 1):
    for y in range(min_y, max_y + 1):
        cur = complex(x, y)
        right = complex(x + 1, y)
        left = complex(x - 1, y)
        if cur in border and right in border and left not in border:
            r_corners.add(cur)
        if cur in border and left in border and right not in border:
            l_corners.add(cur)

interior = set()
for x in range(min_x, max_x + 1):
    inside = False
    n_r_corners = 0
    n_l_corners = 0
    for y in range(min_y, max_y + 1):
        cur = complex(x, y)
        right = complex(x + 1, y)
        left = complex(x - 1, y)

        if cur in border and left in border and right in border:
            inside = not inside
        else:
            if cur in r_corners:
                n_r_corners += 1
            elif cur in l_corners:
                n_l_corners += 1

            if n_r_corners >= 1 and n_l_corners >= 1:
                inside = not inside
                n_r_corners -= 1
                n_l_corners -= 1

        if cur not in border and inside:
            interior.add(cur)

print(len(border | interior))
