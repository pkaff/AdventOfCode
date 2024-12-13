import string
import numpy as np
inputs = [section.split("\n") for section in open("input.txt", "r").read().split("\n\n")]
a_cost = 3
b_cost = 1
res = 0
for section in inputs:
    xa, ya = list(map(lambda x: int(x.strip(string.ascii_letters).strip(string.punctuation)), section[0].split()[2:]))
    xb, yb = list(map(lambda x: int(x.strip(string.ascii_letters).strip(string.punctuation)), section[1].split()[2:]))
    target_x, target_y = list(map(lambda x: int(x.strip(string.ascii_letters).strip(string.punctuation)), section[2].split()[1:]))
    target_x += 10000000000000
    target_y += 10000000000000
    A = np.array([[xa, xb], [ya, yb]])
    B = np.array([[target_x], [target_y]])
    solution = np.linalg.solve(A, B)
    sol_a = round(solution[0][0])
    sol_b = round(solution[1][0])
    if sol_a * xa + sol_b * xb == target_x and sol_a * ya + sol_b * yb == target_y:
        res += a_cost * round(solution[0][0]) + b_cost * round(solution[1][0])
print(res)