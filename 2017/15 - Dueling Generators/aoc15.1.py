inputA = 699
inputB = 124
multA = 16807
multB = 48271
div = 2147483647
mask = (1 << 16) - 1
count = 0
for i in range(40000000):
    inputA = (inputA * multA) % div
    inputB = (inputB * multB) % div
    if (inputA & mask == inputB & mask):
        count += 1
print(count)