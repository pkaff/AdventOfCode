def find_reflection(pattern):
    seen = []
    for ix, line in enumerate(pattern):
        if ix != 0:
            pattern_to_check = pattern[ix:2*ix]
            if pattern_to_check == list(reversed(seen))[:min(len(seen), len(pattern_to_check))]:
                return ix
        seen.append(line)
    return 0

patterns = [[row for row in pattern.split('\n')] for pattern in open("input.txt", "r").read().split('\n\n')]
print(sum([100*find_reflection(pattern) + find_reflection(list(map(list, zip(*list(reversed(pattern)))))) for pattern in patterns]))