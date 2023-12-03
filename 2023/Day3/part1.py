grid = [line.strip() for line in open("input.txt", "r").readlines()]
n_rows = len(grid)
n_cols = len(grid[0])

def get_num_len(s):
    for ix, c in enumerate(s):
        if not str.isdigit(c):
            return ix
    return len(s)

def has_symbol_neighbour(row, col, num_len):
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + num_len + 1):
            if r >= 0 and r < n_rows and c >= 0 and c < n_cols:
                if not str.isdigit(grid[r][c]) and not grid[r][c] == '.':
                    return True
    return False

part_numbers = []
for r_ix, row in enumerate(grid):
    ix = 0
    while ix < n_cols:
        if str.isdigit(row[ix]):
            num_len = get_num_len(row[ix:])
            num = int(row[ix:ix + num_len])
            if has_symbol_neighbour(r_ix, ix, num_len):
                part_numbers.append(num)
            ix += num_len
        else:
            ix += 1
print(sum(part_numbers))

