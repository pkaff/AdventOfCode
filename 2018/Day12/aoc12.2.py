from collections import defaultdict

input = [x.replace('\n', '').replace('initial state: ', '') for x in open("input.txt", "r").readlines()]
emptyPots = ''.join(['.' for _ in range(1000)])
state = emptyPots + input[0] + emptyPots
transforms = [x.split(' => ') for x in input[2:]]
mappedTransforms = defaultdict(str)
for t in transforms:
    mappedTransforms[t[0]] = t[1]
output = 0
diff = 0
for gen in range(1, 1001):
    prevDiff = diff
    prevOutput = output
    output = 0
    state = '..' + ''.join([mappedTransforms[state[i - 2:i + 3]] for i in range(2, len(state) - 2)]) + '..'
    for px in range(state.find('#') - 5, state.rfind('#') + 5):
        if state[px] == '#':
            output += px - 1000
    diff = output - prevOutput
    if diff == prevDiff:
        N = 50000000000
        print(output + (N - gen)*diff)
        break