myin = list(map(int, open("input.txt", "r").readlines()))
print([x * xx for x in myin for xx in myin if x + xx == 2020])