inputs = [int(x) for x in open("input.txt", "r").read().split(",")]
inputs[1] = 12
inputs[2] = 2
index = 0
while inputs[index] != 99:
    opCode = inputs[index]
    op1 = inputs[inputs[index + 1]]
    op2 = inputs[inputs[index + 2]]
    resIx = inputs[index + 3]
    if opCode == 1:
        inputs[resIx] = op1 + op2
    if opCode == 2:
        inputs[resIx] = op1 * op2
    index += 4
print(inputs[0])