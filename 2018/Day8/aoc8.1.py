from collections import defaultdict
input = list(map(lambda x: int(x), open("input.txt", "r").readlines()[0].split(' ')))
ix = 0
depth = 0
nChildren = defaultdict(int)
nMeta = defaultdict(int)
metaSum = 0
while ix < len(input):
	if nChildren[depth] == 0:
		nChildren[depth] = input[ix]
		ix += 1
		nMeta[depth] = input[ix]
		ix += 1
	while nChildren[depth] == 0:
		for mx in range(0, nMeta[depth]):
			metaSum += input[ix + mx]
		ix += nMeta[depth]
		depth -= 1
		if depth == -1:
			break
	if nChildren[depth] != 0:
		nChildren[depth] -= 1
		depth += 1
print(metaSum)
	
	