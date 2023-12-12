from functools import lru_cache
@lru_cache(maxsize=None)
def get_num_arrangements(springs, groups):
    if not groups:
        if springs.count('#') > 0:
            return False, 0
        return True, 1
    group_len = groups[0]
    if sum(groups) > springs.count('?') + springs.count('#'):
        return False, 0
    if group_len == 0:
        if springs and springs[0] == '#':
            return False, 0
        return get_num_arrangements(springs[1:], groups[1:])
    if not springs:
        return False, 0
    if springs[0] == '.':
        return get_num_arrangements(springs[1:], groups)
    assert(springs[0] != '.')
    valid_arrs = 0
    # Try '.'
    valid_dot = False
    if springs[0] != '#':
        valid_dot, num = get_num_arrangements(springs[1:], groups)
        if valid_dot:
            valid_arrs += num
    # Try '#'
    if springs[:group_len].count('.') == 0:
        valid_hash, num = get_num_arrangements(springs[group_len:], (0,) + groups[1:])
    else:
        valid_hash = False
        num = 0
    if valid_hash:
        valid_arrs += num
    return (valid_dot or valid_hash, valid_arrs)

lines = [line.strip().split() for line in open("input.txt", "r").readlines()]
print(sum([get_num_arrangements('?'.join([line] * 5), tuple(map(int, groups.split(',') * 5)))[1] for line, groups in lines]))