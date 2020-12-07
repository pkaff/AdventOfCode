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
        innerBagColor = innerLine[2:].rstrip("s")
        adjList[outerBag].append((nBags, innerBagColor))
        revAdjList[innerBagColor].append(outerBag)

q = queue.Queue()
q.put("shiny gold bag")
visited = ["shiny gold bag"]
while not q.empty():
    bag = q.get()
    for neighbour in revAdjList[bag]:
        if neighbour not in visited:
            visited.append(neighbour)
            q.put(neighbour)
print(len(visited) - 1)
