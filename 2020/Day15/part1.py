myinput = [int(val) for val in open("input.txt", "r").readline().rstrip("\n").split(",")]
lastNbr = 0
mymap = {}
for ix in range(2020):
    if ix < len(myinput):
        lastNbr = myinput[ix]
        mymap[lastNbr] = ix
    else:
        if lastNbr not in mymap:
            mymap[lastNbr] = ix - 1
        if mymap[lastNbr] < ix - 1:
            tmp = lastNbr
            lastNbr = ix - 1 - mymap[lastNbr]
            mymap[tmp] = ix - 1
        else:
            lastNbr = 0
print(lastNbr)
