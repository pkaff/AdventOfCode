import numpy as np
state = 'A'
tape = np.zeros(12386363, dtype=np.int)
ix = 12386363 // 2
for i in range(12386363):
    if state == 'A':
        if tape[ix] == 0:
            tape[ix] = 1
            ix += 1
            state = 'B'
        elif tape[ix] == 1:
            tape[ix] = 0
            ix -= 1
            state = 'E'
    elif state == 'B':
        if tape[ix] == 0:
            tape[ix] = 1
            ix -= 1
            state = 'C'
        elif tape[ix] == 1:
            tape[ix] = 0
            ix += 1
            state = 'A'
    elif state == 'C':
        if tape[ix] == 0:
            tape[ix] = 1
            ix -= 1
            state = 'D'
        elif tape[ix] == 1:
            tape[ix] = 0
            ix += 1
            state = 'C'
    elif state == 'D':
        if tape[ix] == 0:
            tape[ix] = 1
            ix -= 1
            state = 'E'
        elif tape[ix] == 1:
            tape[ix] = 0
            ix -= 1
            state = 'F'
    elif state == 'E':
        if tape[ix] == 0:
            tape[ix] = 1
            ix -= 1
            state = 'A'
        elif tape[ix] == 1:
            ix -= 1
            state = 'C'
    elif state == 'F':
        if tape[ix] == 0:
            tape[ix] = 1
            ix -= 1
            state = 'E'
        elif tape[ix] == 1:
            ix += 1
            state = 'A'
print(np.count_nonzero(tape))