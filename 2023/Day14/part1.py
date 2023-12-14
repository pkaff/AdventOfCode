rocks = [list(row.strip()) for row in open("input.txt", "r").readlines()]
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
rocks = list(map(list, zip(*transposed_rocks)))
print(sum([row.count('O') * (len(rocks) - rix) for rix, row in enumerate(rocks)]))