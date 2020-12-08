import copy
# def parseOp(prevState, visited, op, opIx, acc, backtracked):
#     if backtracked:
#         if op == "nop":
#             op = "jmp"
#         elif op == "jmp":
#             op = "nop"
#         else:
#             raise "unexpected backtracked op"
#     if op == "nop":
#         if not backtracked:
#             prevState.append((opIx, acc, visited))
#         opIx += 1
#     elif op == "acc":
#         acc += int(val)
#         opIx += 1
#     elif op == "jmp":
#         if not backtracked:
#             prevState.append((opIx, acc, visited))
#         opIx += int(val)
#     return opIx, acc

# myinput = [l.rstrip("\n.") for l in open("testinput.txt", "r").readlines()]
# opIx = 0
# acc = 0
# visited = []
# prevState = []
# while True:
#     if opIx == len(myinput):
#         print(acc)
#         break
#     backtracked = False
#     if opIx in visited:
#         print("opix in visited")
#         print(prevState)
#         opIx, acc, visited = prevState.pop()
#         print(opIx)
#         backtracked = True
#         print(visited)
#         print(opIx in visited)
#     op, val = myinput[opIx].split()
#     print(op, val, backtracked)
#     visited.append(opIx)
#     opIx, acc = parseOp(prevState, copy.deepcopy(visited), op, opIx, acc, backtracked)
#     print(opIx)

def runProgram(inp):
    opIx = 0
    acc = 0
    visited = []
    while True:
        if opIx in visited:
            return False, 0
        if opIx == len(inp):
            return True, acc
        op, val = inp[opIx].split()
        visited.append(opIx)
        if op == "nop":
            opIx += 1
        elif op == "acc":
            acc += int(val)
            opIx += 1
        elif op == "jmp":
            opIx += int(val)

myinput = [l.rstrip("\n.") for l in open("input.txt", "r").readlines()]
for i in range(len(myinput)):
    inpCpy = copy.deepcopy(myinput)
    if "nop" in inpCpy[i]:
        inpCpy[i] = inpCpy[i].replace("nop", "jmp")
    elif "jmp" in inpCpy[i]:
        inpCpy[i] = inpCpy[i].replace("jmp", "nop")
    else:
        continue
    done, acc = runProgram(inpCpy)
    if done:
        print(acc)
        break