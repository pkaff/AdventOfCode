from itertools import permutations
myinput = [int(l.rstrip("\n.")) for l in open("input.txt", "r").readlines()]
print([myinput[i] for i in range(25, len(myinput) - 1) if myinput[i] not in map(lambda x: x[0] + x[1], permutations(myinput[i - 25:i], 2))])