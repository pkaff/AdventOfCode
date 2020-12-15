def putToMap(mymap, lastNbr, ix):
    if lastNbr in mymap:
        mymap[lastNbr][1] += 1
    else:
        mymap[lastNbr] = [ix, 1]
myinput = [int(val) for val in open("input.txt", "r").readline().rstrip("\n").split(",")]
lastNbr = 0
mymap = {}
for ix in range(30000000):
    if ix < len(myinput):
        lastNbr = myinput[ix]
        putToMap(mymap, lastNbr, ix)
    else:
        if lastNbr in mymap and mymap[lastNbr][1] > 1:
            lastIx = mymap[lastNbr][0]
            mymap[lastNbr][0] = ix - 1
            lastNbr = mymap[lastNbr][0] - lastIx
            putToMap(mymap, lastNbr, ix)
        elif lastNbr in mymap:
            lastNbr = 0
            putToMap(mymap, lastNbr, ix)
        else:
            lastNbr = 0
            putToMap(mymap, lastNbr, ix)
print(lastNbr)
