from functools import lru_cache
def tilt_north(rocks):
    transposed_rocks = list(map(list, zip(*rocks)))
    for cix, col in enumerate(transposed_rocks):
        start_ix = 0
        new_col = []
        fixed_ixs = [i for i, c in enumerate(col) if c == '#'] + [len(col)]
        for fixed_ix in fixed_ixs:
            to_roll = col[start_ix:fixed_ix]
            if to_roll:
                assert(to_roll.count('#') == 0)
                new_col += ['O'] * to_roll.count('O') + ['.'] * to_roll.count('.')
            if fixed_ix < len(col):
                new_col += ['#']
            start_ix = fixed_ix + 1
        transposed_rocks[cix] = new_col
    return  list(map(list, zip(*transposed_rocks)))

def rotate(rocks):
    return list(map(list, zip(*list(reversed(rocks)))))

def tilt_and_rotate(rocks):
    rocks_list = [list(row.strip()) for row in rocks.split('\n')]
    for _ in range(4):
        rocks_list = tilt_north(rocks_list)
        rocks_list = rotate(rocks_list)
    return '\n'.join([''.join(row) for row in rocks_list])

rocks = open("input.txt", "r").read()
cache = {}
for cur_cycle in range(1, 1000000001):
    rocks = tilt_and_rotate(rocks)
    if rocks in cache:
        n_cycles = cache[rocks]
        cycle_len = (cur_cycle - n_cycles)
        cycles_left = (1000000000 - cur_cycle) % cycle_len
        rocks = list(cache.keys())[list(cache.values()).index(n_cycles + cycles_left)]
        break
    cache[rocks] = cur_cycle

rocks_list = [list(row.strip()) for row in rocks.split('\n')]
print(sum([row.count('O') * (len(rocks_list) - rix) for rix, row in enumerate(rocks_list)]))