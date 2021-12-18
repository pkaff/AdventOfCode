from math import floor, ceil
import re
from itertools import permutations
nbrs = [[int(char) if char.isdigit() else char for char in re.findall(r'\d+|[\[\]]', line)] for line in open("input.txt", "r").readlines()]

def split(snail_lst, pos):
    val = snail_lst[pos]
    return snail_lst[:pos] + ['[', floor(val/2), ceil(val/2), ']'] + snail_lst[pos + 1:]

def explode(snail_lst, pos):
    left_val, right_val = snail_lst[pos:pos + 2]
    for left_pos, val in reversed(list(enumerate(snail_lst[:pos]))):
        if isinstance(val, int):
            snail_lst[left_pos] += left_val
            break
    first_right_ix = pos + 3
    for right_pos, val in enumerate(snail_lst[first_right_ix:]):
        if isinstance(val, int):
            snail_lst[right_pos + first_right_ix] += right_val
            break
    return snail_lst[:pos-1] + [0] + snail_lst[pos + 3:]

def snail_reduce(snail_lst):
    depth = 0
    for pos, val in enumerate(snail_lst):
        if val == '[':
            depth += 1
        elif val == ']':
            depth -= 1
        elif depth > 4:
            return False, explode(snail_lst, pos)

    for pos, val in enumerate(snail_lst):
        if isinstance(val, int) and val >= 10:
            return False, split(snail_lst, pos)

    return True, snail_lst

def snail_reduce_full(snail_lst):
    while True:
        finished, snail_lst = snail_reduce(snail_lst)
        if finished:
            break
    return snail_lst

def magnitude_rec(snail_lst):
    if isinstance(snail_lst, int):
        return snail_lst
    else:
        return 3*magnitude_rec(snail_lst[0]) + 2*magnitude_rec(snail_lst[1])


def magnitude(snail_lst):
    snail_lst = list(map(str, snail_lst))
    snail_str = ','.join(snail_lst)
    snail_str = snail_str.replace('[,[', '[[')
    snail_str = snail_str.replace('],]', ']]')
    snail_str = snail_str.replace('[,', '[')
    snail_str = snail_str.replace(',]', ']')
    snail_lst = eval(snail_str)
    return magnitude_rec(snail_lst)

best_magnitude = 0
for nbr in nbrs:
    for nbr2 in nbrs:
        total = ['['] + nbr + nbr2 + [']']
        total = snail_reduce_full(total)
        mag = magnitude(total)
        best_magnitude = mag if mag > best_magnitude else best_magnitude
print(best_magnitude)