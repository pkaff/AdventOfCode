#hardcoded, found by hand
constraints = {0: (13, lambda w0: w0 - 2), 1: (12, lambda w1: w1 - 3), 2: (11, lambda w2: w2 + 1), 3: (4, lambda w3: w3 - 6), 5: (10, lambda w5: w5 - 8), 6: (7, lambda w6: w6), 8: (9,lambda w8: w8 + 7)}
values = [None]*14
for (first_w_ix, (second_w_ix, second_w_func)) in constraints.items():
    for first_w in range(1, 10):
        second_w = second_w_func(first_w)
        if 0 < second_w <= 9:
            values[first_w_ix] = first_w
            values[second_w_ix] = second_w
            break
print(''.join(map(str, values)))