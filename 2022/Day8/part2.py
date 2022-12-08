eastwest = [[int (height) for height in line.strip()] for line in open("input.txt", "r").readlines()]
gridX = len(eastwest[0])
gridY = len(eastwest)
northsouth = [[None for _ in range(gridY)] for _ in range(gridX)]
max_scenic_score = 0
for rix, row in enumerate(eastwest):
    for cix, dig in enumerate(row):
        northsouth[cix][rix] = dig
for x in range(gridX):
    for y in range(gridY):
        if x == 0 or x == gridX - 1 or y == 0 or y == gridY - 1:
            continue
        row = eastwest[y]
        col = northsouth[x]
        scenic_score = 1
        view_dist = 0
        for tree in reversed(row[:x]):
            view_dist += 1
            if tree >= row[x]:
                break
        scenic_score *= view_dist
        view_dist = 0
        for tree in row[x + 1:]:
            view_dist += 1
            if tree >= row[x]:
                break
        scenic_score *= view_dist
        view_dist = 0
        for tree in reversed(col[:y]):
            view_dist += 1
            if tree >= col[y]:
                break
        scenic_score *= view_dist
        view_dist = 0
        for tree in col[y + 1:]:
            view_dist += 1
            if tree >= col[y]:
                break
        scenic_score *= view_dist
        max_scenic_score = max(max_scenic_score, scenic_score)
print(max_scenic_score)
