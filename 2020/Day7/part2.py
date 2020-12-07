from collections import defaultdict
import queue

myinput = [l.rstrip("\n.") for l in open("input.txt", "r").readlines()]
adjList = defaultdict(list)
revAdjList = defaultdict(list)
for l in myinput:
    outerBag, l2 = l.split("s contain ")
    innerBags = l2.split(", ")
    for innerLine in innerBags:
        nBags = innerLine[0]
        if (nBags == "n"):
            continue
        innerBagColor = innerLine[2:].rstrip("s")
        adjList[outerBag].append((int(nBags), innerBagColor))
        revAdjList[innerBagColor].append(outerBag)

def DFS(adjList, bag, nCurrentBags):
    if not adjList[bag]:
        return 0
    nRecursiveBags = 0
    for nInnerBags, neighbour in adjList[bag]:
        nRecursiveBags += nCurrentBags * nInnerBags
        nRecursiveBags += nCurrentBags * DFS(adjList, neighbour, nInnerBags)
    return nRecursiveBags

print(DFS(adjList, "shiny gold bag", 1))