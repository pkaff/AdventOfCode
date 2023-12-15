def hash(to_hash):
    cur_val = 0
    for c in to_hash:
        cur_val += ord(c)
        cur_val *= 17
        cur_val %= 256
    return cur_val
input = open("input.txt", "r").read().strip().split(',')
seq = []
for s in input:
    op_ix = s.find('=')
    if op_ix == -1:
        op_ix = s.find('-')
    seq.append((s[:op_ix], s[op_ix], int(s[op_ix + 1]) if s[op_ix] == '=' else ''))
hashmap = [[] for _ in range(256)]
for label, op, val in seq:
    hashed = hash(label)
    if op == '-':
        for item in hashmap[hashed]:
            if item[0] == label:
                hashmap[hashed].remove(item)
                break
    if op == '=':
        replaced = False
        for ix, item in enumerate(hashmap[hashed]):
            if item[0] == label:
                hashmap[hashed][ix][1] = val
                replaced = True
        if not replaced:
            hashmap[hashed].append([label, val])
res = 0
for box_num, box in enumerate(hashmap):
    for lense_ix, item in enumerate(box):
        res += (box_num + 1) * (lense_ix + 1) * item[1]
print(res)