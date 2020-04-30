from knothash import makeKnotHash
from collections import defaultdict
global grid
global visited
def canVisit(r, c):
    return (r >= 0 and r < 128 and c >= 0 and c < 128 and not visited[r][c] and grid[r][c] == '1')
def DFS(row, col):
    stack = []
    stack.append([row, col])
    while stack:
        r, c = stack.pop()
        if (not visited[r][c]):
            visited[r][c] = True
        rowNbr = [-1, 0, 0, 1]; #rows of neighbours
        colNbr = [0, -1, 1, 0]; #cols of neighbours
        for k in range(4):
            if canVisit(r + rowNbr[k], c + colNbr[k]):
                stack.append([r + rowNbr[k], c + colNbr[k]])

knothashes = [makeKnotHash("hfdlxzhv" + "-" + str(i)) for i in range(128)]
binaryhashes = []
for k in knothashes:
    binaryhashes.append(''.join(list(map(lambda x: bin(int(x, 16))[2:].zfill(4), k))))
grid = [[binaryhashes[j][i] for i in range(128)] for j in range(128)]
visited = [[False for i in range(128)] for j in range(128)]
nGroups = 0
for r in range(len(binaryhashes)):
    for c in range(len(binaryhashes[r])):
        if not visited[r][c] and grid[r][c] == '1':
            DFS(r, c)
            nGroups += 1
print (nGroups)