from collections import deque
p1, p2 = [deque([int(num) for num in line.split("\n") if ":" not in num]) for line in open("input.txt", "r").read().split("\n\n")]

while p1 and p2:
    v1 = p1.popleft()
    v2 = p2.popleft()
    if v1 > v2:
        p1.append(v1)
        p1.append(v2)
    elif v2 > v1:
        p2.append(v2)
        p2.append(v1)
winner = p1 if p1 else p2
winner.reverse()
print(sum([(ix + 1)*card for ix, card in enumerate(winner)]))