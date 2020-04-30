from collections import defaultdict
input = []
for x in open("input.txt", "r").readlines():
	_, a, _, _, _, _, _, b, _, _ = x.replace('\n', '').split()
	input.append((a, b))
availableNodes = set(a for (a, _) in input) - set(b for (_, b) in input)
visited = []
while len(availableNodes) != 0:
	node = sorted(availableNodes)[0]
	availableNodes.remove(node)
	for n in [b for (a, b) in input if a == node]:
		blocked = any(a for (a, b) in input if b == n and a != node and a not in visited)
		if not blocked:
			availableNodes.add(n)
	visited.append(node)
print(''.join(visited))
 