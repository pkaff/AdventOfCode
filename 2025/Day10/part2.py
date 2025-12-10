from ast import literal_eval
import numpy as np
from scipy.optimize import LinearConstraint
from scipy.optimize import milp

input = [line.strip().split() for line in open("input.txt", "r").readlines()]

def count_presses(buttons, joltage):
    c = np.array([1] * len(buttons))
    a = [[0] * len(buttons) for _ in range(len(joltage))]
    for bidx, button in enumerate(buttons):
        for swix in button:
            a[swix][bidx] = 1
    A = np.array(a)
    b_u = np.array(joltage)
    b_l = b_u
    constraints = LinearConstraint(A, b_l, b_u)
    integrality = np.ones_like(c)
    res = milp(c=c, constraints=constraints, integrality=integrality)
    return res.fun
presses = 0
for row in input:
    buttons = [literal_eval(t) if len(t) > 3 else (literal_eval(t),) for t in row[1:-1]]
    joltage = [int(x) for x in row[-1][1:-1].split(',')]
    presses += count_presses(buttons, joltage)
print(presses)
