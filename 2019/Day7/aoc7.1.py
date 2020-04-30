import sys
import itertools
def RunIntcodeComp(params, inputs):
    def ParseMode(ix, mode):
        if mode == 0:
            return inputs[ix]
        if mode == 1:
            return ix
    def Add(index, mode):
        op1 = inputs[ParseMode(index + 1, mode % 10)]
        op2 = inputs[ParseMode(index + 2, (mode/10) % 10)]
        inputs[ParseMode(index + 3, (mode/100) % 10)] = op1 + op2
        return index + 4, -1
    def Mul(index, mode):
        op1 = inputs[ParseMode(index + 1, mode % 10)]
        op2 = inputs[ParseMode(index + 2, (mode/10) % 10)]
        inputs[ParseMode(index + 3, (mode/100) % 10)] = op1 * op2
        return index + 4, -1
    def In(index, mode):
        inputs[ParseMode(index + 1, mode % 10)] = params.pop()
        return index + 2, -1
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
        return index, -1
    def JIF(index, mode):
        op1 = inputs[ParseMode(index + 1, mode % 10)]
        op2 = inputs[ParseMode(index + 2, (mode/10) % 10)]
        if op1 == 0:
            index = op2
        else:
            index += 3
        return index, -1
    def Less(index, mode):
        op1 = inputs[ParseMode(index + 1, mode % 10)]
        op2 = inputs[ParseMode(index + 2, (mode/10) % 10)]
        inputs[ParseMode(index + 3, (mode/100) % 10)] = int(op1 < op2)
        return index + 4, -1
    def Equals(index, mode):
        op1 = inputs[ParseMode(index + 1, mode % 10)]
        op2 = inputs[ParseMode(index + 2, (mode/10) % 10)]
        inputs[ParseMode(index + 3, (mode/100) % 10)] = int(op1 == op2)
        return index + 4, -1
        
    codeMap = {1: Add, 2: Mul, 3: In, 4: Out, 5: JIT, 6: JIF, 7: Less, 8: Equals}
    index = 0
    res = -1
    
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
    return res
        
sequence = [0, 1, 2, 3, 4]
permutations = itertools.permutations(sequence)
maxThruster = 0
for perm in list(permutations):
    input = 0
    for phaseSetting in perm:
        params = [input, phaseSetting]
        inputs = [int(x) for x in open("input.txt", "r").read().split(",")]
        input = RunIntcodeComp(params, inputs)
    maxThruster = max(maxThruster, input)
print(maxThruster)