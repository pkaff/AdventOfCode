from collections import deque
from itertools import cycle
import numpy as np

output = [int(line) for line in open("testinput.txt", "r").readlines()]

ix_map = np.array(ix for ix in range(len(input)))

for old_ix, num in enumerate(output[:]):
    from_ix = ix_map[old_ix]
    to_ix = (from_ix + num) % len(output)
    if to_ix == from_ix:
        continue
    if from_ix < to_ix:
        output[from_ix:to_ix], output[to_ix] = output[from_ix + 1:to_ix + 1], output[from_ix]
        ix_map[from_ix:to_ix] -= 1
        ix_map[from_ix] = to_ix
    elif from_ix > to_ix:
        output[to_ix], output[to_ix + 2:from_ix + 1] = output[from_ix], output[to_ix + 1:from_ix]
        ix_map[to_ix + 1:from_ix] += 1
        ix_map[from_ix] = to_ix

    break
# look at 2022 day23?