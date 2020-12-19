import re
def splitRule(rule):
    res = []
    splits = rule.split(" | ")
    for split in splits:
        res.append(split.split())
    return res

# def traversePatterns(patterns, compiledSubRules, ix):
#     pattern = patterns[ix]
#     if pattern == [["a"]] or pattern == [["b"]]:
#         return pattern[0][0], None
#     if ix in compiledSubRules:
#         return compiledSubRules[ix]
#     subRule = ""
#     subRules = []
#     for either in pattern:
#         if subRule:
#             subRule += "|"
#         eitherSequence = ""
#         eitherRules = []
#         for nextIx in either:
#             nextSequence, compiledSubRule = traversePatterns(patterns, compiledSubRules, nextIx)
#             eitherSequence += nextSequence
#             eitherRules.append(compiledSubRule)
#         subRule += eitherSequence
#         subRules.append(eitherRules)
#     compiledSubRule = re.compile(subRule)
#     compiledSubRules[ix] = compiledSubRule
#     #return "(" + subRule + ")"
#     return compiledSubRule
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

# def buildRexStr(patterns):
#     rex = "^"
#     rex += traversePatterns(patterns, {}, '0')
#     rex += "$"
#     return rex

rules, inputs = open("input.txt", "r").read().split("\n\n")
rules = rules.replace("\"", "").split("\n")
inputs = inputs.split("\n")
patterns = {}
for rule in rules:
    k, lhs = rule.split(":")
    splitted = splitRule(lhs)
    patterns[k] = splitted

mySum = 0
for test in inputs:
    match, strSubIx = traversePatterns(patterns, "0", test)
    if match and strSubIx == len(test):
        mySum += 1
print(mySum)