import re

class Interval:
    def __init__(self, base, length):
        self.base = base
        self.length = length

    def __contains__(self, num):
        return num >= self.base and num <= self.last()

    def overlaps(self, other):
        return self.base in other or self.last() in other or other.base in self or other.last() in self

    def last(self):
        return self.base + self.length - 1

    def split(self, from_range, dist):
        remaining = []
        splits = []
        if self.base in from_range:
            if self.last() in from_range:
                splits.append(Interval(self.base, self.length).move(dist))
            else:
                splits.append(Interval(self.base, from_range.last() - self.base + 1).move(dist))
                remaining.append(Interval(from_range.last() + 1, self.last() - from_range.last()))
        elif self.last() in from_range:
            remaining.append(Interval(self.base, from_range.base - self.base))
            splits.append(Interval(from_range.base, self.last() - from_range.base + 1).move(dist))
        elif from_range.base in self and from_range.last() in self:
            remaining.append(Interval(self.base, from_range.base - self.base))
            splits.append(Interval(from_range.base, from_range.length).move(dist))
            remaining.append(Interval(from_range.last() + 1, self.last() - from_range.last()))
        else:
            assert(False)

        return splits, remaining

    def move(self, dist):
        self.base += dist
        return self

    def extend(self, other):
        self.length = other.last() - self.base + 1

    def __repr__(self):
        return f'[{self.base}, {self.last()}]'

def merge(seeds):
    seeds = sorted(seeds, key = lambda x: x.base)
    new_seeds = [seeds.pop(0)]
    while seeds:
        seed = seeds.pop(0)
        if seed.overlaps(new_seeds[-1]) or new_seeds[-1].last() == seed.base - 1:
            new_seeds[-1].extend(seed)
        else:
            new_seeds.append(seed)
    return new_seeds

inputs = open("input.txt", "r").read().split('\n\n')
seeds = list(map(int, re.split(': | ', inputs[0])[1:]))
seeds = [Interval(seeds[ix], seeds[ix + 1]) for ix in range(0, len(seeds), 2)]
inputs = [list(map(lambda x: list(map(int, x.split(' '))), mymap.split('\n')[1:])) for mymap in inputs[1:]]
interval_maps = [{Interval(src, leng): Interval(dst, leng) for dst, src, leng in maptype} for maptype in inputs]
for intervals in interval_maps:
    new_seeds = []
    while seeds:
        seed = seeds.pop()
        overlapped = False
        for from_range, to_range in intervals.items():
            if seed.overlaps(from_range):
                splits, remaining = seed.split(from_range, to_range.base - from_range.base)
                seeds += remaining
                new_seeds += splits
                overlapped = True
        if not overlapped:
            new_seeds.append(seed)
    seeds = merge(new_seeds)
print(min([seed.base for seed in seeds]))