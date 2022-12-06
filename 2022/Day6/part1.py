sequence = open("input.txt", "r").read().strip()
for ix in range(3, len(sequence)):
    if len(set(sequence[ix - 3:ix + 1])) == 4:
        print(ix + 1)
        break
