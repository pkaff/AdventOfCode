myIDs = [int(rowcol[:-3], 2) * 8 + int(rowcol[-3:], 2) for rowcol in [''.join(['1' if (c == "B" or c == "R") else '0' for c in l.rstrip()]) for l in open("input.txt", "r").readlines()]]
for row in range(1, 128 - 1):
    for col in range(8):
        id = row * 8 + col
        if id not in myIDs and id - 1 in myIDs and id + 1 in myIDs:
            print(id)
            exit()