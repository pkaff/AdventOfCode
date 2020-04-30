input = [c for c in open("input.txt", "r").readlines()[0]]
for ix in range(len(input) - 2, -1, -1):
	if input[ix + 1].lower() == input[ix].lower():
		if input[ix + 1] != input[ix]:
			del input[ix:ix + 2]
print(len(input))