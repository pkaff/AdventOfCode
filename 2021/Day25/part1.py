from itertools import count

eastfacing_cucumbers = {(x, y) for y, line in enumerate(open("input.txt", "r").readlines()) for x, cucumber in enumerate(line) if cucumber == '>'}
southfacing_cucumbers = {(x, y) for y, line in enumerate(open("input.txt", "r").readlines()) for x, cucumber in enumerate(line) if cucumber == 'v'}
maxX = max(eastfacing_cucumbers, key = lambda pos: pos[0])[0]
maxY = max(eastfacing_cucumbers, key = lambda pos: pos[1])[1]

for step in count(1):
    n_moved = 0
    to_add = set()
    to_remove = set()
    for (x, y) in eastfacing_cucumbers:
        next_pos = ((x + 1) % (maxX + 1), y)
        if next_pos not in eastfacing_cucumbers and next_pos not in southfacing_cucumbers:
            to_remove.add((x,y ))
            to_add.add(next_pos)
    eastfacing_cucumbers -= to_remove
    eastfacing_cucumbers |= to_add
    n_moved += len(to_add)
    to_add.clear()
    to_remove.clear()
    for (x, y) in southfacing_cucumbers:
        next_pos = (x, (y + 1) % (maxY + 1))
        if next_pos not in eastfacing_cucumbers and next_pos not in southfacing_cucumbers:
            to_remove.add((x,y ))
            to_add.add(next_pos)
    southfacing_cucumbers -= to_remove
    southfacing_cucumbers |= to_add
    n_moved += len(to_add)
    if n_moved == 0:
        print(step)
        break