from difflib import ndiff
import sys
input = [''.join(x).replace('\n','') for x in open("input1.txt", "r").readlines()]
for ix in range(0, len(input) - 1):
	for kx in range(ix + 1, len(input)):
		if (len([li for li in ndiff(input[ix], input[kx]) if li[0] == ' ']) == len(input[ix]) - 1):
			print(input[ix])
			print(input[kx])
			sys.exit()