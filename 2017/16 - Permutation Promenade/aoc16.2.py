import string
from collections import deque
from collections import defaultdict
global dance
def DoDance(n, d, programs):
    states = defaultdict(lambda: False)
    for i in range(n):
        danceIx = 0
        for k in range(d, len(dance)):
            m = dance[k]
            hsh = ''.join(programs) + str(danceIx)
            if states[hsh]:
                return i, danceIx
            else:
                states[hsh] = True
            if m[0] == 's':
                programs.rotate(int(m[1:]))
            if m[0] == 'x':
                mid = m.index('/')
                programs[int(m[1:mid])], programs[int(m[mid+1:])] = programs[int(m[mid+1:])], programs[int(m[1:mid])]
            if m[0] == 'p':
                a, b = programs.index(m[1]), programs.index(m[3])
                programs[a], programs[b] = programs[b], programs[a]
            danceIx += 1
    return n, 0
            
file = open("input.txt", "r")
dance = file.read().split(',')
programs = deque(list(map(chr, range(ord('a'), ord('p') + 1))))
initialPos = deque(list(map(chr, range(ord('a'), ord('p') + 1))))
fullItrs, danceIx = DoDance(1000000000, 0, programs)
fullDanceLeft = 1000000000 % fullItrs
DoDance(fullDanceLeft, danceIx, programs)
print(''.join(programs))