from itertools import cycle
myinput = [7, 1, 6, 8, 9, 2, 5, 4, 3]
for r in range(100):
    curCycle = cycle(myinput)
    dest = next(curCycle) - 1
    pickedup = [next(curCycle) for _ in range(3)]
    if dest == 0:
        dest = max(myinput)
    while dest in pickedup:
        dest -= 1
        if dest == 0:
            dest = max(myinput)
    destIx = myinput.index(dest) + 1
    myinput[1:destIx] = myinput[4:destIx] + pickedup
    myinput[-1], myinput[:-1] = myinput[0], myinput[1:]
finalIx = myinput.index(1)
myinput[finalIx + 1 :], myinput[: finalIx] = myinput[: finalIx], myinput[finalIx + 1 :]
print("".join([str(i) for i in myinput if i != 1]))