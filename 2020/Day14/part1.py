myinput = [l.rstrip("\n") for l in open("input.txt", "r").readlines()]
onMask = 0
offMask = 0
registries = {}
for line in myinput:
    if 'mask =' in line:
        mask = line[7:].replace("X", "0")
        onMask = int(mask, 2)
        mask = line[7:].replace("X", "1")
        offMask = int(mask, 2)
    else:
        lhs, rhs = line.split(" = ")
        registry = int(lhs[4:-1])
        value = int(rhs)
        value |= onMask
        value &= offMask
        registries[registry] = value
print(sum(registries.values()))