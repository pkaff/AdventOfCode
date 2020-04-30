import re
from collections import defaultdict

def exec_command(func):
    def final(before, instr):
        after = list(before)
        after[instr[2]] = func(before, instr[0], instr[1])
        return after
    return final

addr = exec_command(lambda before,a,b: before[a] + before[b])
addi = exec_command(lambda before,a,b: before[a] + b)
mulr = exec_command(lambda before,a,b: before[a] * before[b])
muli = exec_command(lambda before,a,b: before[a] * b)
banr = exec_command(lambda before,a,b: before[a] & before[b])
bani = exec_command(lambda before,a,b: before[a] & b)
borr = exec_command(lambda before,a,b: before[a] | before[b])
bori = exec_command(lambda before,a,b: before[a] | b)
setr = exec_command(lambda before,a,_: before[a])
seti = exec_command(lambda before,a,_: a)
gtir = exec_command(lambda before,a,b: 1 if a > before[b] else 0)
gtri = exec_command(lambda before,a,b: 1 if before[a] > b else 0)
gtrr = exec_command(lambda before,a,b: 1 if before[a] > before[b] else 0)
eqir = exec_command(lambda before,a,b: 1 if a == before[b] else 0)
eqri = exec_command(lambda before,a,b: 1 if before[a] == b else 0)
eqrr = exec_command(lambda before,a,b: 1 if before[a] == before[b] else 0)

commands = [addr, addi,
            mulr, muli,
            banr, bani,
            borr, bori,
            setr, seti,
            gtir, gtri, gtrr,
            eqir, eqri, eqrr]
commandsMap = {'addr': 0, 'addi': 1,
            'mulr': 2, 'muli': 3,
            'banr': 4, 'bani': 5,
            'borr': 6, 'bori': 7,
            'setr': 8, 'seti': 9,
            'gtir': 10, 'gtri': 11, 'gtrr': 12,
            'eqir': 13, 'eqri': 14, 'eqrr': 15}

def callCommand(instr):
    return commands[commandsMap[instr]]
input = [l.strip() for l in open("input.txt", "r").readlines()]

#registers = [0, 0, 0, 0, 0, 0]
registers = [1, 0, 0, 0, 0, 0]
ipIx = list(map(int, re.findall('-?\d+', input[0])))[0]
input = input[1:]
ip = 0
count = 0
while ip < len(input) and count <= 36:
    l = input[ip]
    registers[ipIx] = ip
    instr = l.split()[0]
    params = list(map(int, re.findall('-?\d+', l)))
    registers = callCommand(instr)(registers, params)
    ip = registers[ipIx]
    print(instr, params, registers)
    ip += 1
    count += 1
print(registers[0])