def find_reflection(pattern, old_ix):
    seen = []
    for ix, line in enumerate(pattern):
        if ix != 0:
            pattern_to_check = pattern[ix:2*ix]
            if pattern_to_check == list(reversed(seen))[:min(len(seen), len(pattern_to_check))] and ix != old_ix:
                return ix
        seen.append(line)
    return 0

def switch_char(c):
    if c == '#':
        return '.'
    return '#'

def switch_chars(pattern):
    transposed_pattern = list(map(list, zip(*list(reversed(pattern)))))
    old_reflection_rix = find_reflection(pattern, 0)
    old_reflection_cix = find_reflection(transposed_pattern, 0)
    for rix in range(len(pattern)):
        for cix in range(len(pattern[0])):
            fixed_pattern = [p[:] for p in pattern]
            fixed_pattern[rix][cix] = switch_char(fixed_pattern[rix][cix])
            new_reflection_rix = find_reflection(fixed_pattern, old_reflection_rix)
            if new_reflection_rix != 0 and new_reflection_rix != old_reflection_rix:
                return new_reflection_rix * 100
            fixed_transposed_pattern = [p[:] for p in transposed_pattern]
            fixed_transposed_pattern[cix][rix] = switch_char(fixed_transposed_pattern[cix][rix])
            new_reflection_cix = find_reflection(fixed_transposed_pattern, old_reflection_cix)
            if new_reflection_cix != 0 and new_reflection_cix != old_reflection_cix:
                return new_reflection_cix

patterns = [[list(row) for row in pattern.split('\n')] for pattern in open("input.txt", "r").read().split('\n\n')]
print(sum([switch_chars(pattern) for pattern in patterns]))