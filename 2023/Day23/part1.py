forest = {(x, y): c for y, row in enumerate(open("input.txt", "r").readlines()) for x, c in enumerate(row.strip())}
max_x = max(forest, key=lambda k: k[0])[0]
max_y = max(forest, key=lambda k: k[1])[1]
start = (1, 0)
end = (max_x - 1, max_y)
forest[(1, -1)] = '#'
forest[(max_x - 1, max_y + 1)] = '#'
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

to_visit = [(start, [])]
paths = []
while to_visit:
    cur, path = to_visit.pop()
    if cur == end:
        paths.append(len(path))
    for dir in dirs:
        neighbour = (cur[0] + dir[0], cur[1] + dir[1])
        next_c = forest[neighbour]
        if next_c != '#' and neighbour not in path:
            if next_c != '.':
                if (next_c == '>' and dir == (1, 0)) or (next_c == '^' and dir == (0, -1)) or (next_c == '<' and dir == (-1, 0)) or (next_c == 'v' and dir == (0, 1)):
                    to_visit.append((neighbour, path + [cur]))
            else:
                to_visit.append((neighbour, path + [cur]))
print(max(paths))