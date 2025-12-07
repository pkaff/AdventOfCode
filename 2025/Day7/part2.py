from collections import defaultdict
filelines = open("input.txt", "r").readlines()
input = {(col, row): True for row, line in enumerate(filelines) for col, c in enumerate(line.strip()) if c == '^'}
cols = {filelines[0].find('S'): 1}
height = len(filelines)
for row in range(1, height):
    new_cols = defaultdict(lambda: 0)
    for col in cols:
        if (col, row) in input:
            new_cols[col - 1] += cols[col]
            new_cols[col + 1] += cols[col]
        else:
            new_cols[col] += cols[col]
    cols = new_cols
print(sum(cols.values()))