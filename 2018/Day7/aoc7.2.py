from collections import defaultdict
input = []
for x in open("input.txt", "r").readlines():
	_, a, _, _, _, _, _, b, _, _ = x.replace('\n', '').split()
	input.append((a, b))
availableNodes = set(a for (a, _) in input) - set(b for (_, b) in input)
time = 0
visited = []
workers = [0 for _ in range(5)]
workerNodes = ['' for _ in range(5)]
while True:
	if min(workers) > time:
		time = min(workers)
		continue
	
	available = [wi for (wi, t) in enumerate(workers) if t <= time]
	for wi in available:
		if workerNodes[wi] != '':
			visited.append(workerNodes[wi])
	for wi in available:
		node = workerNodes[wi]
		if node == '':
			continue
		
		for n in [b for (a, b) in input if a == node]:
			blocked = any(a for (a, b) in input if b == n and a != node and a not in visited)
			if not blocked:
				availableNodes.add(n)
		
		workerNodes[wi] = ''
		
	for wi in available:
		if len(availableNodes) == 0:
			break
			
		node = sorted(availableNodes)[0]
		availableNodes.remove(node)
		workerNodes[wi] = node
		
		workers[wi] = time + ord(node) - 4
		
	if all(node == '' for node in workerNodes):
		break
		
	time += 1

print(''.join(visited))
print(time)