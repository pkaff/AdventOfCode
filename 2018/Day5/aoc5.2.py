import string
[[],[],[]]
input = [c for c in open("input.txt", "r").readlines()[0]]
minLen = len(input)
for c in string.ascii_lowercase:
	tmp = [s for s in input if s.lower() != c]
	for ix in range(len(tmp) - 2, -1, -1):
		if ix == len(tmp) - 1:
			continue
		if tmp[ix + 1].lower() == tmp[ix].lower():
			if tmp[ix + 1] != tmp[ix]:
				del tmp[ix:ix + 2]
	minLen = min(minLen, len(tmp))
print(minLen)