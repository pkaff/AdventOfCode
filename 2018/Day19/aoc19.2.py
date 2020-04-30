i4 = 10551293
out = 0
for i in range(1, i4 + 1):
    if i4 % i == 0:
        print(i)
        out += i
print(out)