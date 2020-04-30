from collections import defaultdict

def RecursiveMax(nodes, root, lastIx, visited):
    if (root in visited):
        return []
    visited.append(root)
    f, s = root.split('/')
    if f == lastIx:
        nextIx = s
    else:
        nextIx = f
    maxes = []
    for nextNode in nodes[nextIx]:
        maxes.append(RecursiveMax(nodes, nextNode, nextIx, visited[:]))
    ret = max(maxes, key=lambda x: len(x))
    ret.append(root)
    return ret
        
file = open("input.txt", "r")
components = file.readlines()
nodes = defaultdict(list)
for comp in components:
    nodes[comp.strip().split('/')[0]].append(comp.strip())
    nodes[comp.strip().split('/')[1]].append(comp.strip())

longestBridges = []
for root in nodes['0']:
    visited = []
    longestBridges.append(RecursiveMax(nodes, root, '0', visited))

strongestBridge = 0
for lb in longestBridges:
    bridgeStr = 0
    for n in lb:
        f, s = n.split('/')
        bridgeStr += int(f) + int(s)
    strongestBridge = max(strongestBridge, bridgeStr)
print(strongestBridge)