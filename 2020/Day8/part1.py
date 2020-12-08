myinput = [l.rstrip("\n.") for l in open("input.txt", "r").readlines()]
opIx = 0
acc = 0
visited = []
while True:
    if opIx in visited:
        print(acc)
        break
    op, val = myinput[opIx].split()
    visited.append(opIx)
    if op == "nop":
        opIx += 1
    elif op == "acc":
        acc += int(val)
        opIx += 1
    elif op == "jmp":
        opIx += int(val)