from itertools import product
inputs = open("input.txt", "r").read().split('\n\n')
keys = []
locks = []
height = len(inputs[0].split('\n')) - 2
for input in inputs:
    pattern = input.split('\n')
    if all(c=='#' for c in pattern[0]):
        lock = []
        for col in range(len(pattern[0])):
            count = -1
            for row in range(len(pattern)):
                c = pattern[row][col]
                if c == '#':
                    count += 1
            lock.append(count)
        locks.append(lock)
    else:
        key = []
        for col in range(len(pattern[0])):
            count = -1
            for row in range(len(pattern)):
                c = pattern[row][col]
                if c == '#':
                    count += 1
            key.append(count)
        keys.append(key)
res = 0
for key, lock in product(keys, locks):
    if all(k + l <= height for k, l in zip(key, lock)):
        res += 1
print(res)