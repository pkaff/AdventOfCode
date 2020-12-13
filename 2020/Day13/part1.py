from math import floor
myinput = [l.rstrip("\n") for l in open("input.txt", "r").readlines()]
firstTime = int(myinput[0])
ids = [int(myid) for myid in myinput[1].split(",") if myid != "x"]
bestBus = min(list(map(lambda x: ((floor(firstTime/x) + 1) * x, x), ids)))
print(bestBus[1] * (bestBus[0] - firstTime))