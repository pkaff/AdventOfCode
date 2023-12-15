def hash(to_hash):
    cur_val = 0
    for c in to_hash:
        cur_val += ord(c)
        cur_val *= 17
        cur_val %= 256
    return cur_val
seq = open("input.txt", "r").read().strip().split(',')
print(sum([hash(s) for s in seq]))