myin = list(map(int, open("input.txt", "r").readlines()))
three_elem_window = list(map(sum, zip(myin[:-2], myin[1:-1], myin[2:])))
print(sum(1 if b > a else 0 for (a, b) in zip(three_elem_window[:-1], three_elem_window[1:])))
