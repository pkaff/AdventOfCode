from functools import lru_cache
input = [int(line.strip()) for line in open("input.txt", "r").readlines()]
@lru_cache(maxsize=None)
def calc_secret_num(secret_num):
    multiplier = secret_num * 64
    secret_num ^= multiplier
    secret_num %= 16777216
    divisor = secret_num // 32
    secret_num ^= divisor
    secret_num %= 16777216
    multiplier = secret_num * 2048
    secret_num ^= multiplier
    secret_num %= 16777216
    return secret_num

unique_seqs = set()
max_seqs = []
for secret_num in input:
    last_digits = [secret_num % 10]
    for _ in range(2000):
        secret_num = calc_secret_num(secret_num)
        last_digits.append(secret_num % 10)
    diffs = [second - first for first, second in zip(last_digits[:-1], last_digits[1:])]
    max_seq = {}
    for seq, price in zip(zip(diffs[:-4], diffs[1:-3], diffs[2:-2], diffs[3:-1]), last_digits[4:]):
        tseq = tuple(seq)
        if tseq not in max_seq:
            max_seq[tseq] = price
        unique_seqs.add(tseq)
    max_seqs.append(max_seq)
print(max(sum([max_seq[seq] if seq in max_seq else 0 for max_seq in max_seqs]) for seq in unique_seqs))