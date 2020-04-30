from collections import defaultdict
input = [tuple(map(int, y.split(', '))) for y in [x.replace('\n','') for x in open("input.txt", "r").readlines()]]
minX = min(input, key=lambda i: i[0])[0]
maxX = max(input, key=lambda i: i[0])[0]
minY = min(input, key=lambda i: i[1])[1]
maxY = max(input, key=lambda i: i[1])[1]
gridX = range(minX - int(10000/len(input)), maxX + int(10000/len(input)))
gridY = range(minY - int(10000/len(input)), maxY + int(10000/len(input)))
regionSize = 0
for xx in gridX:
	for yy in gridY:
		totalDist = 0
		for point in input:
			manhattanDist = abs(point[0] - xx) + abs(point[1] - yy)
			totalDist += manhattanDist
			if totalDist > 10000:
				break
		if totalDist < 10000:
			regionSize += 1
print(regionSize)