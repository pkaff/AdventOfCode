myin = list(map(int, open("input.txt", "r").readlines()))
print([x * xx * xxx for x in myin for xx in myin for xxx in myin if x + xx + xxx == 2020])