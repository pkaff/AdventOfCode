file = open("input.txt", "r")
memory = list(map(int, file.read().split()))
for i in range(2):
    hashes = []
    while str(memory) not in hashes:
        hashes.append(str(memory))
        maxIx = memory.index(max(memory))
        maxVal = memory[maxIx]
        memory[maxIx] = 0
        for i in range(1, maxVal + 1):
            memory[(maxIx + i) % len(memory)] += 1
print(len(hashes))