from collections import defaultdict
input = [tuple(map(int, y.split(', '))) for y in [x.replace('\n','') for x in open("input.txt", "r").readlines()]]
minX = min(input, key=lambda i: i[0])[0]
maxX = max(input, key=lambda i: i[0])[0]
minY = min(input, key=lambda i: i[1])[1]
maxY = max(input, key=lambda i: i[1])[1]
grid = defaultdict(list)
areaCount = defaultdict(int)
for xx in range(minX, maxX + 1):
	for yy in range(minY, maxY + 1):
		closests = []
		closestDist = 2*(maxX + maxY)
		for point in input:
			manhattanDist = abs(point[0] - xx) + abs(point[1] - yy)
			if manhattanDist < closestDist:
				closestDist = manhattanDist
				closests.clear()
				closests.append(point)
			elif manhattanDist == closestDist:
				closests.append(point)
		grid[xx, yy] = closests
		if len(closests) == 1:
			areaCount[closests[0]] += 1
for xx in range(minX, maxX + 1):
	for yy in [minY, maxY]:
		for c in grid[xx, yy]:
			if c in input:
				input.remove(c)
for yy in range(minY, maxY + 1):
	for xx in [minX, maxX]:
		for c in grid[xx, yy]:		
			if c in input:
				input.remove(c)
maxArea = 0
for pair in input:
	maxArea = max(areaCount[pair], maxArea)
print(maxArea)
	