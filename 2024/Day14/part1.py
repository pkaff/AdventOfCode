from collections import Counter
from functools import reduce
from operator import mul
inputs = [line.strip().split() for line in open("input.txt", "r").readlines()]
inputs = [(list(map(int, line[0][2:].split(','))), list(map(int, line[1][2:].split(',')))) for line in inputs]
width = 101
height = 103
iterations = 100
moved = Counter([((pos[0] + vel[0]*iterations) % width, (pos[1] + vel[1]*iterations) % height) for pos, vel in inputs])
q1 = sum([moved[pos] for pos in moved if pos[0] < width // 2 and pos[1] < height // 2])
q2 = sum([moved[pos] for pos in moved if pos[0] > width // 2 and pos[1] < height // 2])
q3 = sum([moved[pos] for pos in moved if pos[0] < width // 2 and pos[1] > height // 2])
q4 = sum([moved[pos] for pos in moved if pos[0] > width // 2 and pos[1] > height // 2])
print(reduce(mul, [q1, q2, q3, q4]))