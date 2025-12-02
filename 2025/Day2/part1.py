ids = open("input.txt", "r").readline().strip().split(',')
def get_sum_silly(idrange):
    start, end = idrange.split('-')
    print(idrange)
    if len(start) % 2 != 0:
        h1 = "1" + "0"*(len(start)//2)
        h2 = "0"*(len(start)//2 + 1)
    else:
        h1, h2 = start[0:len(start)//2], start[len(start)//2:]
    sum_silly = 0
    while int(h1 + h2) <= int(end):
        if h1 == h2:
            sum_silly += int(h1 + h2)
        if int(h2) < int(h1):
            h2 = h1
        else:
            h1 = str(int(h1) + 1)
            h2 = "0"*len(h1)
    return sum_silly
print(sum(get_sum_silly(idrange) for idrange in ids))