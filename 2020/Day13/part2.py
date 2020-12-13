from math import gcd
from functools import reduce
def lcm(x, y):
    return abs(x * y) // gcd(x, y)
myinput = [l.rstrip("\n") for l in open("input.txt", "r").readlines()]
#expected = int(myinput[0]) # for test cases with expected output
enumeratedIds = [(ix, int(myid)) for ix, myid in enumerate(myinput[1].split(",")) if myid != "x"]
period = enumeratedIds[0][1]
timeDiffs = [(ix, myid) for ix, myid in enumeratedIds[1:]]
t = 0
while timeDiffs:
    t += period
    alignedIds = [myid for timeDiff, myid in timeDiffs if (t + timeDiff) % myid == 0]
    if alignedIds:
        period = reduce(lcm, [period] + alignedIds)
        timeDiffs = [(timeDiff, myid) for timeDiff, myid in timeDiffs if myid not in alignedIds]
print(t)