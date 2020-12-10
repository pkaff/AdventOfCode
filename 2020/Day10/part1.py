myinput = [0] + [int(l.rstrip("\n.")) for l in open("input.txt", "r").readlines()]
myinput.sort()
myinput += [myinput[-1] + 3]
counts = [myinput[i] - myinput[i - 1] for i in range(1, len(myinput)) if myinput[i] - myinput[i - 1] == 1 or myinput[i] - myinput[i - 1] == 3]
print(counts.count(1) * counts.count(3))