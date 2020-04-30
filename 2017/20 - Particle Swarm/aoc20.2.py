import re
from collections import defaultdict
file = open("input.txt", "r")
particles = [[eval(re.sub('[pav=]', '', re.sub('>', ']', re.sub('<', '[', coords.rstrip(','))))) for coords in line.split()] for line in file.readlines()]
while True:
    ixToRemove = defaultdict(list)
    for ix in range(len(particles)):
        ixToRemove[','.join(map(str, particles[ix][0]))].append(ix)
    listIxToRemove = []
    for pos, ixList in ixToRemove.items():
        if len(ixList) > 1:
            for ix in ixList:
                listIxToRemove.append(ix)
    listIxToRemove.sort()
    for ix in reversed(listIxToRemove):
        del particles[ix]
    print(len(particles))
    for particle in particles:
        for ix in range(3):
            particle[1][ix] += particle[2][ix]
            particle[0][ix] += particle[1][ix]