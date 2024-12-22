input = [int(line.strip()) for line in open("input.txt", "r").readlines()]
res = 0
for secret_num in input:
    for _ in range(2000):
        multiplier = secret_num * 64
        secret_num ^= multiplier
        secret_num %= 16777216
        divisor = secret_num // 32
        secret_num ^= divisor
        secret_num %= 16777216
        multiplier = secret_num * 2048
        secret_num ^= multiplier
        secret_num %= 16777216
    res += secret_num
print(res)