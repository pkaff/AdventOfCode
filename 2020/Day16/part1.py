import re
patterns, myticket, othertickets = open("input.txt", "r").read().split("\n\n")
patterns = [re.findall(r"\b\d+-\d+\b", l) for l in patterns.split("\n")]
patterns = list(map(lambda rs: [range(int(myrange.split('-')[0]), int(myrange.split('-')[1]) + 1) for myrange in rs], patterns))
myticket = [int(v) for v in myticket.split("\n")[1].split(",")]
othertickets = [[int(v) for v in l.split(",")] for l in othertickets.split("\n")[1:]]
scanningErrorRate = 0
for ticket in othertickets:
    for val in ticket:
        if not any(list(map(lambda rs: val in rs[0] or val in rs[1], patterns))):
            scanningErrorRate += val
print(scanningErrorRate)