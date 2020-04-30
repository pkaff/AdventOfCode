from collections import defaultdict

input = [x.replace('\n', '').replace('initial state: ', '') for x in open("input.txt", "r").readlines()]
emptyPots = ''.join(['.' for _ in range(24)])
state = emptyPots + input[0] + emptyPots
transforms = [x.split(' => ') for x in input[2:]]
mappedTransforms = defaultdict(str)
for t in transforms:
	mappedTransforms[t[0]] = t[1]
for gen in range(20):
	state = '..' + ''.join([mappedTransforms[state[i - 2:i + 3]] for i in range(2, len(state) - 2)]) + '..'
output = 0
print(state)
for px in range(len(state)):
	if state[px] == '#':
		output += px - 24
print(output)