from collections import defaultdict
input = [x.replace('\n','').replace(' @', ':').split(': ') for x in open("input1.txt", "r").readlines()]
fabric = [[[] for x in range(1500)] for y in range(1500)]
overlaps = defaultdict(set)
ids = []
for i in input:
	id = int(i[0].replace('#',''))
	ids.append(id)
	coords = [int(x) for x in i[1].split(',')]
	x = coords[0] + 1
	y = coords[1] + 1
	sizes = [int(x) for x in i[2].split('x')]
	dx = sizes[0]
	dy = sizes[1]
	for xx in range(x, x + dx):
		for yy in range(y, y + dy):
			if fabric[xx][yy]:
				for n in fabric[xx][yy]:
					overlaps[n].add(id)
					overlaps[id].add(n)
			fabric[xx][yy].append(id)
for id in ids:
	if len(overlaps[id]) == 0:
		print(id)
        break