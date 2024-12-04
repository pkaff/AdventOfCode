input = [line.strip() for line in open("input.txt", "r").readlines()]
def get_char(rix, cix):
    if rix >= 0 and rix < len(input) and cix >= 0 and cix < len(input[rix]):
        return input[rix][cix]
    return '.'
def count_xmas(rix, cix):
    dirs = [(d, tuple(map(lambda x: -x, d))) for d in [(1, 1), (-1, -1), (-1, 1), (1, -1)]]
    words = [''.join([get_char(rix + startr + k*dr, cix + startc + k*dc) for k in range(3)]) for ((startr, startc), (dr, dc)) in dirs]
    return 1 if words.count('MAS') >= 2 else 0
res = sum([count_xmas(rix, cix) for rix in range(len(input)) for cix in range(len(input[rix]))])
print(res)