declarations = [dict()]
myinput = [l.strip() for l in open("input.txt", "r").readlines()]
for line in myinput:
    if not line:
        declarations.append(dict())
    else:
        for q in line:
            declarations[-1][q] = True
print(sum([len(groupDecl) for groupDecl in declarations]))
