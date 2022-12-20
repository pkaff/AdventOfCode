from collections import deque

decryption_key = 811589153
input = [int(line) * decryption_key for line in open("input.txt", "r").readlines()]

output = deque(input)
ix_map = deque([ix for ix in range(len(input))])

for _ in range(10):
    for old_ix, num in enumerate(input):
        if num == 0:
            continue

        new_ix = ix_map.index(old_ix)
        del output[new_ix]
        del ix_map[new_ix]

        output.rotate(-num)
        ix_map.rotate(-num)

        output.insert(new_ix, num)
        ix_map.insert(new_ix, old_ix)
zero_ix = output.index(0)
ixs_to_find = [(zero_ix + k*1000) % len(output) for k in range(1, 4)]
print(sum([output[ix] for ix in ixs_to_find]))