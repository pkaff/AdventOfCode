from itertools import permutations
myinput = [int(l.rstrip("\n.")) for l in open("input.txt", "r").readlines()]
target = [myinput[i] for i in range(25, len(myinput) - 1) if myinput[i] not in map(lambda x: x[0] + x[1], permutations(myinput[i - 25:i], 2))][0]
lowIx = 0
highIx = 1
while sum(myinput[lowIx:highIx]) != target:
    if sum(myinput[lowIx:highIx]) < target:
        highIx += 1
    elif sum(myinput[lowIx:highIx]) > target:
        lowIx += 1
print(min(myinput[lowIx:highIx]) + max(myinput[lowIx:highIx]))