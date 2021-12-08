import sys
myin = list(map(int, open("input.txt", "r").read().replace('\n', '').split(',')))
minstart = min(myin)
maxstart = max(myin)
min_fuel = sys.maxsize
for mid_point in range(minstart, maxstart + 1):
    fuel = sum([sum(range(1, abs(mid_point - val) + 1)) for val in myin])
    if fuel > min_fuel:
        break
    min_fuel = fuel
print(min_fuel)
