from collections import defaultdict

def traverse(input):
	nChildren, nMeta = input[:2]
	input = input[2:]
	values = []
	
	for i in range(0, nChildren):
		value, input = traverse(input)
		values.append(value)
		
	if nChildren == 0:
		return (sum(input[:nMeta]), input[nMeta:])
	else:
		return (sum([values[ix - 1] for ix in input[:nMeta] if ix != 0 and ix <= len(values)]), input[nMeta:])

input = list(map(lambda x: int(x), open("input.txt", "r").readlines()[0].split(' ')))
(value, _) = traverse(input)
print(value)
