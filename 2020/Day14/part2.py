from itertools import product
myinput = [l.rstrip("\n") for l in open("input.txt", "r").readlines()]
masks = []
registries = {}
for line in myinput:
    if 'mask =' in line:
        mask = line[7:]
        nFloating = mask.count("X")
        combinations = list(product(["0", "1"], repeat=nFloating))
        nullMask = mask.replace("0", "1").replace("X", "0")
        masks = [int(nullMask, 2)]
        for comb in combinations:
            combMask = mask
            for combChar in comb:
                combMask = combMask.replace("X", combChar, 1)
            masks.append(int(combMask, 2))
    else:
        lhs, rhs = line.split(" = ")
        registry = int(lhs[4:-1])
        value = int(rhs)
        nullMask = masks[0]
        for mask in masks[1:]:
            newRegistry = (registry & nullMask) | mask
            registries[newRegistry] = value
print(sum(registries.values()))