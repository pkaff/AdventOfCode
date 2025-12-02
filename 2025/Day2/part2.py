ids = open("testinput.txt", "r").readline().strip().split(',')
def get_silly_inner(start, end, length):
    print(start, end, length)
    while len(start) % length != 0:
        start = "1" + "0"*len(start)
    #print(start)
    repeat_part = start[:length]
    num_parts = len(start) // length
    sillies = set()
    print(repeat_part, num_parts)
    while int(repeat_part * num_parts) <= int(end):
        if num_parts > 1 and int(repeat_part * num_parts) >= int(start):
            print(f"silly: {repeat_part * num_parts}")
            sillies.add(int(repeat_part * num_parts))
        print(f"repeat_part: {repeat_part}")
        if all([p == '9' for p in repeat_part]):
            repeat_part = "1" + "0"*(len(repeat_part) - 1)
            num_parts += 1
        else:
            repeat_part = str(int(repeat_part) + 1)
        print(f"repeat_part: {repeat_part}")
    return sillies
def get_sum_silly(idrange):
    start, end = idrange.split('-')
    print(idrange)
    ids = set()
    for silly_set in [get_silly_inner(start, end, k) for k in range(1, len(end)//2 + 1)]:
        ids |= silly_set
    print(ids)
    return sum(ids)
print(sum(get_sum_silly(idrange) for idrange in ids))

#34023488892 low