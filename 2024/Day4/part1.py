input = [line.strip() for line in open("input.txt", "r").readlines()]
def get_char(rix, cix):
    if rix >= 0 and rix < len(input) and cix >= 0 and cix < len(input[rix]):
        return input[rix][cix]
    return '.'
def count_xmas(rix, cix):
    dirs = [(dr, dc) for dr in range(-1, 2) for dc in range(-1, 2)]
    words = [''.join([get_char(rix + k*dr,cix + k*dc) for k in range(4)]) for dr, dc in dirs]
    return words.count('XMAS')
res = sum([count_xmas(rix, cix) for rix in range(len(input)) for cix in range(len(input[rix]))])
print(res)