input = [''.join(x).replace('\n','') for x in open("input1.txt", "r").readlines()]
unique = [''.join(set(x)) for x in input]
dupl = 0
tripl = 0
for i, u in zip(input, unique):
	foundDupl = False
	foundTripl = False
	for c in u:
		nOccur = i.count(c)
		if nOccur == 2:
			foundDupl = True
		if nOccur == 3:
			foundTripl = True
	if foundDupl:
		dupl += 1
	if foundTripl:
		tripl += 1
print(dupl * tripl)