from collections import defaultdict

def RecursiveMax(nodes, root, lastIx, visited):
    if (root in visited):
        return 0
    visited.append(root)
    f, s = root.split('/')
    if f == lastIx:
        nextIx = s
    else:
        nextIx = f
    maxes = []
    for nextNode in nodes[nextIx]:
        maxes.append(RecursiveMax(nodes, nextNode, nextIx, visited[:]))
    return int(f) + int(s) + max(maxes)
        
file = open("input.txt", "r")
components = file.readlines()
nodes = defaultdict(list)
for comp in components:
    nodes[comp.strip().split('/')[0]].append(comp.strip())
    nodes[comp.strip().split('/')[1]].append(comp.strip())
maxStr = 0
for root in nodes['0']:
    visited = []
    maxStr = max(maxStr, RecursiveMax(nodes, root, '0', visited))
print(maxStr)