low, high = map(int, open("input.txt", "r").readline().split("-"))
nValids = 0
for password in range(low, high + 1):
    passwordString = str(password)
    valid = True
    digitCount = {}
    for (d1, d2) in zip(map(int, passwordString), map(int, passwordString[1:])):
        if d2 < d1:
            valid = False
            break
        if d1 == d2:
            if d1 in digitCount:
                digitCount[d1] += 1
            else:
                digitCount[d1] = 2
    if valid and 2 in digitCount.values():
        nValids += 1
print(nValids)