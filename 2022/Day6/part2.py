sequence = open("input.txt", "r").read().strip()
for ix in range(13, len(sequence)):
    if len(set(sequence[ix - 13:ix + 1])) == 14:
        print(ix + 1)
        break
