myin = list(map(int, open("input.txt", "r").readlines()))
print(sum(1 if b > a else 0 for (a, b) in list(zip(myin[:-1], myin[1:]))))
