myin = ''.join([format(int(hexchar, 16), '0>4b') for hexchar in open("input.txt", "r").read().replace('\n', '')])
ix = 0
version_sum = 0
while int(myin[ix:], 2) != 0:
    version = myin[ix:ix+3]
    version_sum += int(version, 2)
    ix += 3
    typeid = myin[ix:ix+3]
    ix += 3
    if int(typeid, 2) == 4:
        prefix_ix = ix
        while myin[prefix_ix] == '1':
            prefix_ix += 5
        ix = prefix_ix + 5
    else:
        length_id = myin[ix]
        ix += 1
        if length_id == '0':
            subpacket_len = int(myin[ix:ix+15], 2)
            ix += 15
        elif length_id == '1':
            num_sub_packets = int(myin[ix:ix+11], 2)
            ix += 11
print(version_sum)