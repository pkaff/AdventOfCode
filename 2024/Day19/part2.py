from functools import lru_cache
towels, patterns = open("input.txt", "r").read().split('\n\n')
towels = tuple(towels.strip().split(', '))
patterns = patterns.split('\n')

@lru_cache(maxsize=None)
def count_patterns(available_towels, pattern):
    if pattern == "":
        return 1
    count = 0
    for offset in range(1, len(pattern) + 1):
        if pattern[:offset] in available_towels:
            count += count_patterns(available_towels, pattern[offset:])
    return count
print(sum([count_patterns(towels, pattern) for pattern in patterns]))