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
    subRule = ""
    for either in pattern:
        if subRule:
            subRule += "|"
        eitherSequence = ""
        for nextIx in either:
            eitherSequence += buildRexStr(patterns, nextIx)
        subRule += eitherSequence
    return "(?:" + subRule + ")"
def traversePatterns(patterns, ix, testStr):
    pattern = patterns[ix]
    if pattern == [["a"]] or pattern == [["b"]]:
        #print(testStr)
        matched = pattern[0][0] == testStr[0]
        return matched, 1
    for either in pattern:
        strSubIx = 0
        matchedAll = True
        for nextIx in either:
            #print("recur with ix ", nextIx, " str: ", testStr, " subStr: ", testStr[strSubIx:], " strsubix ", strSubIx)
            matched, nLettersHandled = traversePatterns(patterns, nextIx, testStr[strSubIx:])
            # if matched:
            #     print(testStr[strSubIx:], " matched pattern", nextIx)
            # else:
            #     print(testStr[strSubIx:], " didn't match pattern", nextIx)
            matchedAll &= matched
            if matched:
                strSubIx += nLettersHandled
            else:
                break
        if matchedAll:
            #print("matched all, strsubix ", strSubIx)
            return True, strSubIx
    return False, 0


rules, inputs = open("input2.txt", "r").read().split("\n\n")
rules = rules.replace("\"", "").split("\n")
inputs = inputs.split("\n")
patterns = {}
for rule in rules:
    k, lhs = rule.split(":")
    splitted = splitRule(lhs)
    patterns[k] = splitted

mySum = 0
pat1 = buildRexStr(patterns, "42")
print(pat1)
pat2 = buildRexStr(patterns, "31")
print(pat2)
#0: (42 | 42 8)(42 31 | 42 11 31)
for test in inputs:
    if re.match("^" + pat1 + "+" + pat2 + "+" + "$", test):
        mySum += 1
print(mySum)