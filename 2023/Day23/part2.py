from collections import defaultdict
forest = {(x, y): c for y, row in enumerate(open("input.txt", "r").readlines()) for x, c in enumerate(row.strip())}
max_x = max(forest, key=lambda k: k[0])[0]
max_y = max(forest, key=lambda k: k[1])[1]
start = (1, 0)
end = (max_x - 1, max_y)
forest[(1, -1)] = '#'
forest[(max_x - 1, max_y + 1)] = '#'
slopes = ['>', '<', 'v', '^']
dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
junctions = {(x, y) for (x, y), c in forest.items() if c == '.' if len([(x + dir[0], y + dir[1]) for dir in dirs if forest[(x + dir[0], y + dir[1])] in slopes]) > 1}
junctions.add(end)

def get_next_juncs(pos):
    juncs = []
    to_visit = [(pos, 0, {pos})]
    while to_visit:
        cur, steps, visited = to_visit.pop(0)
        if cur in junctions and cur != pos:
            juncs.append((cur, steps))
            continue
        for dir in dirs:
            neighbour = (cur[0] + dir[0], cur[1] + dir[1])
            next_c = forest[neighbour]
            if next_c != '#' and neighbour not in visited:
                to_visit.append((neighbour, steps + 1, visited | {neighbour}))
    return juncs

to_visit = [(start)]
visited = []
junc_lens = defaultdict(lambda: [])
while to_visit:
    cur = to_visit.pop()
    if cur in visited:
        continue
    visited.append(cur)
    for neighbour, n_steps in get_next_juncs(cur):
        junc_lens[cur].append((neighbour, n_steps))
        if neighbour not in visited:
            to_visit.append(neighbour)

to_visit = [(0, start, {start})]
max_length = 0
while to_visit:
    cur_steps, cur, visited = to_visit.pop()
    if cur == end:
        max_length = max(max_length, cur_steps)
        continue
    for neighbour, n_steps in junc_lens[cur]:
        if neighbour not in visited:
            to_visit.append((cur_steps + n_steps, neighbour, visited | {neighbour}))
print(max_length)