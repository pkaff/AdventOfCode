from statistics import mean
myin = list(map(int, open("input.txt", "r").read().replace('\n', '').split(',')))
print(sum([sum(range(1, abs(int(mean(myin) - 0.5) - val) + 1)) for val in myin]))
