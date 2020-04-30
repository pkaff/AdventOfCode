from collections import defaultdict
inputs = [r.strip().split(")") for r in open("input.txt", "r").readlines()]
directOrbits = defaultdict(list)
for parent, child in inputs:
    directOrbits[parent].append(child)
def traverseTree(depth, key):
    if len(directOrbits[key]) == 0:
        return depth
    childOrbits = 0
    for child in directOrbits[key]:
        childOrbits += traverseTree(depth + 1, child)
    return depth + childOrbits
print(traverseTree(0, "COM"))
    