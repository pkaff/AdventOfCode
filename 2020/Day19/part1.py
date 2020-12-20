import re
def splitRule(rule):
    res = []
    splits = rule.split(" | ")
    for split in splits:
        res.append(split.split())
    return res

def buildRexStr(patterns, ix):
    pattern = patterns[ix]
    if pattern == [["a"]] or pattern == [["b"]]:
        return pattern[0][0]
    resultingRexs = []
    for either in pattern:
        resultingRexs.append("(" + ")(".join([buildRexStr(patterns, nextIx) for nextIx in either]) + ")")
    return "|".join(resultingRexs)

rules, inputs = open("input2.txt", "r").read().split("\n\n")
rules = rules.replace("\"", "").split("\n")
inputs = inputs.split("\n")
patterns = {}
for rule in rules:
    k, lhs = rule.split(":")
    splitted = splitRule(lhs)
    patterns[k] = splitted

print(sum([bool(re.fullmatch(buildRexStr(patterns, "0"), test)) for test in inputs]))