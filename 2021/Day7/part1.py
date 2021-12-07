from statistics import median
myin = list(map(int, open("input.txt", "r").read().replace('\n', '').split(',')))
print(sum([abs(int(median(myin)) - val) for val in myin]))
