from operator import mul
from functools import reduce
input = [line.strip().split() for line in open("input.txt", "r").readlines()]
nums = [[int(num) for num in row] for row in input[:-1]]
#transpose
nums = list(map(list, zip(*nums)))
ops = input[-1]
total = 0
for ix, op in enumerate(ops):
    if op == '*':
        total += reduce(mul, nums[ix], 1)
    elif op == '+':
        total += sum(nums[ix])
print(total)