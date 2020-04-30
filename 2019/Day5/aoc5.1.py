import sys
inputs = [int(x) for x in open("input.txt", "r").read().split(",")]
input = 1
index = 0

def ParseMode(ix, mode):
    if mode == 0:
        return inputs[ix]
    if mode == 1:
        return ix
def Add(mode):
    global index
    op1 = inputs[ParseMode(index + 1, mode % 10)]
    op2 = inputs[ParseMode(index + 2, (mode/10) % 10)]
    inputs[ParseMode(index + 3, (mode/100) % 10)] = op1 + op2
    index += 4
def Mul(mode):
    global index
    op1 = inputs[ParseMode(index + 1, mode % 10)]
    op2 = inputs[ParseMode(index + 2, (mode/10) % 10)]
    inputs[ParseMode(index + 3, (mode/100) % 10)] = op1 * op2
    index += 4
def In(mode):
    global index
    inputs[ParseMode(index + 1, mode % 10)] = input
    index += 2
def Out(mode):
    global index
    op = inputs[ParseMode(index + 1, mode % 10)]
    print(op)
    index += 2
def Done(mode):
    print("Finished")
    sys.exit()
    
codeMap = {1: Add, 2: Mul, 3: In, 4: Out, 99: Done}

while True:
    instr = str(inputs[index])
    opCode = int(instr[-2:])
    mode = instr[:-2]
    if not mode:
        mode = 0
    mode = int(mode)
    codeMap[opCode](mode)