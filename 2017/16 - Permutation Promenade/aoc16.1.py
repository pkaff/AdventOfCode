import string
from collections import deque
file = open("input.txt", "r")
dance = file.read().split(',')
programs = deque(list(map(chr, range(ord('a'), ord('p') + 1))))
for m in dance:
    if m[0] == 's':
        programs.rotate(int(m[1:]))
    if m[0] == 'x':
        mid = m.index('/')
        programs[int(m[1:mid])], programs[int(m[mid+1:])] = programs[int(m[mid+1:])], programs[int(m[1:mid])]
    if m[0] == 'p':
        a, b = programs.index(m[1]), programs.index(m[3])
        programs[a], programs[b] = programs[b], programs[a]
print(''.join(programs))