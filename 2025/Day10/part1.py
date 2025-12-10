from functools import lru_cache
from ast import literal_eval
import sys
from frozendict import frozendict

sys.setrecursionlimit(10**6)
input = [line.strip().split() for line in open("testinput.txt", "r").readlines()]
def count_presses(target, buttons, bests, cur, num_presses):
    if cur == target:
        return num_presses
    if cur in bests:
        return bests[cur]
    new_bests = dict(bests)
    new_bests[cur] = num_presses

    min_presses = sys.maxsize
    for button in buttons:
        new_cur = list(cur)
        for strix in button:
            new_cur[strix] = '.' if new_cur[strix] != '.' else '#'
        min_presses = min(count_presses(target, buttons, frozendict(new_bests), ''.join(new_cur), num_presses + 1), min_presses)
    return min_presses
    
presses = 0
for row in input:
    goal = row[0][1:-1]
    buttons = tuple(literal_eval(t) if len(t) > 3 else (literal_eval(t),) for t in row[1:-1])
    presses += count_presses(goal, buttons, frozendict(), '.' * len(goal), 0)
print(presses)