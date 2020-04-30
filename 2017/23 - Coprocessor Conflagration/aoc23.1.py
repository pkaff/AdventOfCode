from collections import defaultdict

file = open("input.txt", "r")
instructions = file.readlines()
registers = defaultdict(lambda: 0)
i = 0
nMul = 0
while i < len(instructions):
    parts = instructions[i].split()
    val = 0
    if parts[2].isalpha():
        val = registers[parts[2]]
    else:
        val = int(parts[2])
    if parts[0] == 'set':
        registers[parts[1]] = val
    if parts[0] == 'sub':
        registers[parts[1]] -= val
    if parts[0] == 'mul':
        registers[parts[1]] *= val
        nMul += 1
    if parts[0] == 'mod':
        if val != 0:
            registers[parts[1]] %= val
    if parts[0] == 'jnz':
        jnzVal = 0
        if parts[1].isalpha():
            jnzVal = registers[parts[1]]
        else:
            jnzVal = int(parts[1])
        if jnzVal != 0:
            i += val - 1
    i += 1
print(nMul)