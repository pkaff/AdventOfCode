from collections import defaultdict
file = open("input.txt", "r")
instructions = file.readlines()
registers = defaultdict(lambda: 0)
lastPlayedFreq = 0
i = 0
while i < len(instructions):
    parts = instructions[i].split()
    if parts[0] == 'snd':
        lastPlayedFreq = registers[parts[1]]
    elif parts[0] == 'rcv':
        if registers[parts[1]] != 0:
            registers[parts[1]] = lastPlayedFreq
            print(lastPlayedFreq)
            break
    else:
        val = 0
        if parts[2] in registers:
            val = registers[parts[2]]
        else:
            val = int(parts[2])
        if parts[0] == 'set':
            registers[parts[1]] = val
        if parts[0] == 'add':
            registers[parts[1]] += val
        if parts[0] == 'mul':
            registers[parts[1]] *= val
        if parts[0] == 'mod':
            if val != 0:
                registers[parts[1]] %= val
        if parts[0] == 'jgz':
            if registers[parts[1]] > 0:
                i += val - 1
    i += 1