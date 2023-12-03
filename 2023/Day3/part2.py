grid = [line.strip() for line in open("input.txt", "r").readlines()]
n_rows = len(grid)
n_cols = len(grid[0])
gears = {(r_ix, c_ix):[] for r_ix, row in enumerate(grid) for c_ix, c in enumerate(row) if c == '*'}

def get_num_len(s):
    for ix, c in enumerate(s):
        if not str.isdigit(c):
            return ix
    return len(s)

def add_num_to_gears(row, col, num_len, num):
    for r in range(row - 1, row + 2):
        for c in range(col - 1, col + num_len + 1):
            if r >= 0 and r < n_rows and c >= 0 and c < n_cols:
                if grid[r][c] == '*':
                    gears[(r, c)].append(num)

for r_ix, row in enumerate(grid):
    ix = 0
    while ix < n_cols:
        if str.isdigit(row[ix]):
            num_len = get_num_len(row[ix:])
            num = int(row[ix:ix + num_len])
            add_num_to_gears(r_ix, ix, num_len, num)
            ix += num_len
        else:
            ix += 1
print(sum([nums[0] * nums[1] for nums in gears.values() if len(nums) == 2]))

