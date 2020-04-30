import numpy as np
import re
import math
from collections import defaultdict

def fillMatrix(pattern, matrix):
    row = 0
    col = 0
    for c in pattern:
        if c == '.':
            matrix[row][col] = 0
        elif c == '/':
            col = 0
            row += 1
            continue
        col += 1
    return matrix
def blockshaped(arr, nrows, ncols):
    h, w = arr.shape
    return arr.reshape(h//nrows, nrows, -1, ncols).swapaxes(1, 2).reshape(-1, nrows, ncols)

file = open("input.txt", "r")
patterns = file.readlines()
inputPatterns = defaultdict(lambda: '')
for pattern in patterns:
    re.sub('#', '1', re.sub('.', '0', pattern))
    inp, outp = pattern.split(' => ')
    if len(inp) == 5:
        m = np.ones((2, 2), dtype=np.int)
        n = np.ones((3, 3), dtype=np.int)
    if len(inp) == 11:
        m = np.ones((3, 3), dtype=np.int)
        n = np.ones((4, 4), dtype=np.int)
    m = fillMatrix(inp, m)
    n = fillMatrix(outp, n)
    for j in range(4):
        inputPatterns[m.tostring()] = n
        inputPatterns[np.flipud(m).tostring()] = n
        inputPatterns[np.flipud(m).tostring()] = n
        inputPatterns[np.fliplr(m).tostring()] = n
        m = np.rot90(m)

fractalArt = np.array([[0,1,0],[0,0,1],[1,1,1]])
for i in range(5):
    if fractalArt.size % 2 == 0:
        bSize = 2
        splits = int(fractalArt.size / 4)
    elif fractalArt.size % 3 == 0:
        bSize = 3
        splits = int(fractalArt.size / 9)
    blockMatrices = blockshaped(fractalArt, bSize, bSize)
    newBlockMatrices = []
    for blockMatrix in blockMatrices:
        newBlockMatrices.append(inputPatterns[blockMatrix.tostring()])
    sqrtSize = int(math.sqrt(len(newBlockMatrices)))
    newbSize = bSize + 1
    fractalArt = np.empty([sqrtSize*newbSize, sqrtSize*newbSize], dtype=int)
    k = 0
    for nBM in newBlockMatrices:
        fractalArt[newbSize*(k // sqrtSize):newbSize*(k // sqrtSize)+newbSize, newbSize*(k % sqrtSize):newbSize*(k % sqrtSize)+newbSize] = nBM
        k += 1
print(np.count_nonzero(fractalArt))