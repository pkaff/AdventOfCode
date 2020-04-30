def genA():
    inputA = 699
    multA = 16807
    div = 2147483647
    while True:
        inputA = (inputA * multA) % div
        if (inputA % 4 == 0):
            yield inputA

def genB():
    inputB = 124
    multB = 48271
    div = 2147483647
    while True:
        inputB = (inputB * multB) % div
        if (inputB % 8 == 0):
            yield inputB
            
mask = (1 << 16) - 1
count = 0
aGen = genA()
bGen = genB()
for i in range(5000000):
    inputA = next(aGen)
    inputB = next(bGen)
    if (inputA & mask == inputB & mask):
        count += 1
print(count)
