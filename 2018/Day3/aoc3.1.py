input = [x.replace('\n','').replace(' @', ':').split(': ') for x in open("input1.txt", "r").readlines()]
input2 = [y for x in input for y in x if ',' in y or 'x' in y]
fabric = [[0 for x in range(1500)] for y in range(1500)]
it = iter(input2)
for i in it:
	coords = [int(x) for x in i.split(',')]
	x = coords[0] + 1
	y = coords[1] + 1
	sizes = [int(x) for x in next(it).split('x')]
	dx = sizes[0]
	dy = sizes[1]
	for xx in range(x, x + dx):
		for yy in range(y, y + dy):
			fabric[xx][yy] += 1

sqInches = 0
for x in range(len(fabric)):
	for y in range(len(fabric[x])):
		if fabric[x][y] > 1:
			sqInches += 1
	
print(sqInches)