import re
patterns, myticket, othertickets = open("input.txt", "r").read().split("\n\n")
patternNames = [l.split(":")[0] for l in patterns.split("\n")]
patterns = [re.findall(r"\b\d+-\d+\b", l) for l in patterns.split("\n")]
patterns = list(map(lambda rs: [range(int(myrange.split('-')[0]), int(myrange.split('-')[1]) + 1) for myrange in rs], patterns))
myticket = [int(v) for v in myticket.split("\n")[1].split(",")]
othertickets = [[int(v) for v in l.split(",")] for l in othertickets.split("\n")[1:]]
validTickets = []
for ticket in othertickets:
    keep = True
    for val in ticket:
        if not any(list(map(lambda rs: val in rs[0] or val in rs[1], patterns))):
            keep = False
            break
    if keep:
        validTickets.append(ticket)
ticketFields = list(zip(*validTickets))
usedPatterns = []
usedFields = []
res = 1
while len(usedPatterns) < len(patterns):
    for patternIx, pattern in enumerate(patterns):
        if patternIx in usedPatterns:
            continue
        nPatternMatches = 0
        foundFieldIx = -1
        for fieldIx, fieldValues in enumerate(ticketFields):
            if fieldIx in usedFields:
                continue
            if all(list(map(lambda fieldValue: fieldValue in pattern[0] or fieldValue in pattern[1], fieldValues))):
                nPatternMatches += 1
                foundFieldIx = fieldIx
        if nPatternMatches == 1:
            usedPatterns.append(patternIx)
            usedFields.append(foundFieldIx)
            if "departure" in patternNames[patternIx]:
                res *= myticket[foundFieldIx]
print(res)