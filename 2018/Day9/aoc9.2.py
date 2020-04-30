from collections import defaultdict
from collections import deque
import re

nPlayers, lastMarble = map(int, re.findall(r'\d+', open("input.txt", "r").readlines()[0]))
marbles = deque()
marbles.append(0)
curPlayer = 0
scores = defaultdict(int)
for marble in range(1, 100*lastMarble):
	if marble % 23 == 0:
		marbles.rotate(7)
		scores[curPlayer] += marble + marbles.pop()
		marbles.rotate(-1)
	else:
		marbles.rotate(-1)
		marbles.append(marble)
	curPlayer = (curPlayer + 1) % nPlayers

print(max(scores.values()))