from functools import lru_cache
towels, patterns = open("input.txt", "r").read().split('\n\n')
towels = tuple(towels.strip().split(', '))
patterns = patterns.split('\n')

@lru_cache(maxsize=None)
def find_pattern(available_towels, pattern):
    if pattern == "":
        return True
    for offset in range(1, len(pattern) + 1):
        if pattern[:offset] in available_towels:
            if find_pattern(available_towels, pattern[offset:]):
                return True
    return False
print(sum([1 for pattern in patterns if find_pattern(towels, pattern)]))