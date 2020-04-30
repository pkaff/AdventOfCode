from collections import defaultdict
import re

nPlayers, lastMarble = map(int, re.findall(r'\d+', open("input.txt", "r").readlines()[0]))

marbles = [0]
curMarbleIx = 0
curPlayer = 0
scores = defaultdict(int)
for marble in range(1, lastMarble):
	if marble % 23 == 0:
		scores[curPlayer] += marble
		curMarbleIx = abs((curMarbleIx - 7) % len(marbles))
		scores[curPlayer] += marbles.pop(curMarbleIx)
	else:
		nextMarbleIx = (curMarbleIx + 2) % len(marbles)
		if nextMarbleIx == 0:
			marbles.append(marble)
			curMarbleIx = len(marbles) - 1
		else:
			marbles.insert(nextMarbleIx, marble)
			curMarbleIx = nextMarbleIx
	curPlayer = (curPlayer + 1) % nPlayers

print(max(scores.values()))