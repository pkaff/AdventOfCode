from collections import deque
from itertools import islice
p1, p2 = [deque([int(num) for num in line.split("\n") if ":" not in num]) for line in open("input.txt", "r").read().split("\n\n")]

def recursiveCombat(p1, p2):
    prevPlayStates = {}
    while p1 and p2:
        if str(p1) + str(p2) in prevPlayStates:
            return 0
        prevPlayStates[str(p1) + str(p2)] = True
        v1 = p1.popleft()
        v2 = p2.popleft()
        if v1 <= len(p1) and v2 <= len(p2):
            winner = recursiveCombat(deque(islice(p1, 0, v1)), deque(islice(p2, 0, v2)))
        else:
            winner = int(v1 < v2)
        if winner == 0:
            p1.append(v1)
            p1.append(v2)
        elif winner == 1:
            p2.append(v2)
            p2.append(v1)
    return 0 if p1 else 1

winner = p1 if recursiveCombat(p1, p2) == 0 else p2
winner.reverse()
print(sum([(ix + 1)*card for ix, card in enumerate(winner)]))