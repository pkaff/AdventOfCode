def countRecursiveCombinations(myinput, ix, memory):
    if ix == 0:
        return 1
    if ix in memory.keys():
        return memory[ix]
    mem = 0
    start = 0 if ix - 3 < 0 else ix - 3
    for nextIx in range(start, ix):
        if myinput[ix] - myinput[nextIx] <= 3:
            mem += countRecursiveCombinations(myinput, nextIx, memory)
    memory[ix] = mem
    return mem

myinput = [0] + [int(l.rstrip("\n.")) for l in open("input.txt", "r").readlines()]
myinput.sort()
myinput += [myinput[-1] + 3]
memory = {}
print(countRecursiveCombinations(myinput, len(myinput) - 1, memory))