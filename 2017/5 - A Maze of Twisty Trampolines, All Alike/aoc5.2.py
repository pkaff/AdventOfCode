file = open("input.txt", "r")
jumps = list(map(int, file.read().splitlines()))
ix = 0
nJumps = 0
while ix >= 0 and ix < len(jumps):
	prevIx = ix
	ix += jumps[ix]
	if jumps[prevIx] >= 3:
		jumps[prevIx] -= 1
	else:
		jumps[prevIx] += 1
	nJumps += 1
print (nJumps)
