print(max([int(rowcol[:-3], 2) * 8 + int(rowcol[-3:], 2) for rowcol in [''.join(['1' if (c == "B" or c == "R") else '0' for c in l.rstrip()]) for l in open("input.txt", "r").readlines()]]))