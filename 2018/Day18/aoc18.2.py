from copy import deepcopy

prevState = [[c for c in l.strip()] for l in open("input.txt", "r").readlines()]
states = []
for m in range(1, 1000):
    state = deepcopy(prevState)
    for y in range(len(state)):
        for x in range(len(state[y])):
            curAcre = state[y][x]
            nAdjacentTrees = 0
            nAdjacentLumberyards = 0
            for xx in range(-1, 2):
                for yy in range(-1, 2):
                    if xx == 0 and yy == 0:
                        continue
                    if 0 <= x + xx < len(prevState[y]) and 0 <= y + yy < len(prevState):
                        if prevState[y + yy][x + xx] == '#':
                            nAdjacentLumberyards += 1
                        elif prevState[y + yy][x + xx] == '|':
                            nAdjacentTrees += 1
            if curAcre == '.' and nAdjacentTrees >= 3:
                state[y][x] = '|'
            elif curAcre == '|' and nAdjacentLumberyards >= 3:
                state[y][x] = '#'
            elif curAcre == '#' and (nAdjacentTrees < 1 or nAdjacentLumberyards < 1):
                state[y][x] = '.'
    strHash = '\n'.join(''.join(r) for r in state)
    if strHash in states:
        ix = states.index(strHash)
        period = m - (ix + 1)
        while (ix + 1) % period != 1000000000 % period:
            ix += 1
        nLumberyards = states[ix].count('#')
        nTrees = states[ix].count('|')
        print(nLumberyards * nTrees)
        break
    states.append(strHash)
    prevState = state