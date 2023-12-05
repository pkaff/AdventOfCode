import re

class Interval:
    def __init__(self, base, length):
        self.base = base
        self.length = length

    def __contains__(self, num):
        return num >= self.base and num < self.base + self.length

    def __repr__(self):
        return f'[{self.base}, {self.base + self.length - 1}]'

inputs = open("input.txt", "r").read().split('\n\n')
seeds = list(map(int, re.split(': | ', inputs[0])[1:]))
inputs = [list(map(lambda x: list(map(int, x.split(' '))), mymap.split('\n')[1:])) for mymap in inputs[1:]]
interval_maps = [{Interval(src, leng): Interval(dst, leng) for dst, src, leng in maptype} for maptype in inputs]
for intervals in interval_maps:
    for seed_ix, seed in enumerate(seeds):
        for from_range, to_range in intervals.items():
            if seed in from_range:
                seeds[seed_ix] += to_range.base - from_range.base
print(min(seeds))