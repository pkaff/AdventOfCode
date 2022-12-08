eastwest = [[int (height) for height in line.strip()] for line in open("input.txt", "r").readlines()]
gridX = len(eastwest[0])
gridY = len(eastwest)
northsouth = [[None for _ in range(gridY)] for _ in range(gridX)]
visible = dict()
for rix, row in enumerate(eastwest):
    for cix, dig in enumerate(row):
        northsouth[cix][rix] = dig
        visible[(cix, rix)] = True
for x in range(gridX):
    for y in range(gridY):
        if x == 0 or x == gridX - 1 or y == 0 or y == gridY - 1:
            continue
        else:
            row = eastwest[y]
            col = northsouth[x]
            if row[x] <= max(row[x + 1:]) and row[x] <= max(row[:x]) and col[y] <= max(col[y + 1:]) and col[y] <= max(col[:y]):
                visible[(x, y)] = False
print(sum(1 for v in visible.values() if v))
