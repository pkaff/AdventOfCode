import re
from collections import defaultdict

def exec_command(func):
    def final(before, instr):
        after = list(before)
        after[instr[3]] = func(before, instr[1], instr[2])
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

def nSimilar(instr, before, after):
    count = 0
    for c in commands:
        res = c(before, instr)
        if res == after:
            count += 1
    return count
        
input, input2 = open("input.txt", "r").read().split('\n\n\n')
input = input.strip().split('\n')
count = 0
for i in input:
    if i == '':
        continue
    if 'Before' in i:
        before = list(map(int, re.findall('-?\d+', i)))
    elif 'After' in i:
        after = list(map(int, re.findall('-?\d+', i)))
        if nSimilar(instr, before, after) >= 3:
            count += 1
    else:
        instr = list(map(int, re.findall('-?\d+', i)))
print(count)