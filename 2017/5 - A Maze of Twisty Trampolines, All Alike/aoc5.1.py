file = open("input.txt", "r")
jumps = list(map(int, file.read().splitlines()))
ix = 0
nJumps = 0
while ix >= 0 and ix < len(jumps):
	jumps[ix] += 1
	ix += jumps[ix] - 1
	nJumps += 1
print (nJumps)
