filelines = open("input.txt", "r").readlines()
input = {(col, row): True for row, line in enumerate(filelines) for col, c in enumerate(line.strip()) if c == '^'}
cols = {filelines[0].find('S')}
height = len(filelines)
splits = 0
for row in range(1, height):
    new_cols = set()
    for col in cols:
        if (col, row) in input:
            new_cols.add(col - 1)
            new_cols.add(col + 1)
            splits += 1
        else:
            new_cols.add(col)
    cols = new_cols
print(splits)