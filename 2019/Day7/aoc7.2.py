import sys
import itertools
def RunIntcodeComp(index, params, inputs):
    def ParseMode(ix, mode):
        if mode == 0:
            return inputs[ix]
        if mode == 1:
            return ix
    def Add(index, mode):
        op1 = inputs[ParseMode(index + 1, mode % 10)]
        op2 = inputs[ParseMode(index + 2, (mode/10) % 10)]
        inputs[ParseMode(index + 3, (mode/100) % 10)] = op1 + op2
        return index + 4, None
    def Mul(index, mode):
        op1 = inputs[ParseMode(index + 1, mode % 10)]
        op2 = inputs[ParseMode(index + 2, (mode/10) % 10)]
        inputs[ParseMode(index + 3, (mode/100) % 10)] = op1 * op2
        return index + 4, None
    def In(index, mode):
        inputs[ParseMode(index + 1, mode % 10)] = params.pop(0)
        return index + 2, None
    def Out(index, mode):
        op = inputs[ParseMode(index + 1, mode % 10)]
        return index + 2, op
    def JIT(index, mode):
        op1 = inputs[ParseMode(index + 1, mode % 10)]
        op2 = inputs[ParseMode(index + 2, (mode/10) % 10)]
        if op1 != 0:
            index = op2
        else:
            index += 3
        return index, None
    def JIF(index, mode):
        op1 = inputs[ParseMode(index + 1, mode % 10)]
        op2 = inputs[ParseMode(index + 2, (mode/10) % 10)]
        if op1 == 0:
            index = op2
        else:
            index += 3
        return index, None
    def Less(index, mode):
        op1 = inputs[ParseMode(index + 1, mode % 10)]
        op2 = inputs[ParseMode(index + 2, (mode/10) % 10)]
        inputs[ParseMode(index + 3, (mode/100) % 10)] = int(op1 < op2)
        return index + 4, None
    def Equals(index, mode):
        op1 = inputs[ParseMode(index + 1, mode % 10)]
        op2 = inputs[ParseMode(index + 2, (mode/10) % 10)]
        inputs[ParseMode(index + 3, (mode/100) % 10)] = int(op1 == op2)
        return index + 4, None
        
    codeMap = {1: Add, 2: Mul, 3: In, 4: Out, 5: JIT, 6: JIF, 7: Less, 8: Equals}
    res = None
    
    while True:
        instr = str(inputs[index])
        opCode = int(instr[-2:])
        if opCode == 99:
            break
        mode = instr[:-2]
        if not mode:
            mode = 0
        mode = int(mode)
        index, res = codeMap[opCode](index, mode)
        if res is not None:
            break
    return index, res, params

sequence = [5, 6, 7, 8, 9]
permutations = itertools.permutations(sequence)
maxThruster = 0
inputs = [int(x) for x in open("input.txt", "r").read().split(",")]
for perm in list(permutations):
    amplifierInputs = []
    amplifierParams = []
    for ix in range(5):
        amplifierInputs.append(inputs[:])
        amplifierParams.append([perm[ix]])
    input = 0
    amplifierIxs = [0] * 5
    while input is not None:
        for ix in range(5):
            amplifierParams[ix].append(input)
            amplifierIxs[ix], input, amplifierParams[ix] = RunIntcodeComp(amplifierIxs[ix], amplifierParams[ix], amplifierInputs[ix])
        thruster = thruster if input is None else input
    maxThruster = max(maxThruster, thruster)

print(maxThruster)