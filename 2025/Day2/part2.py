ids = open("input.txt", "r").readline().strip().split(',')
def if_silly(myid):
    if len(myid) < 2:
        return False
    for length in range(1, len(myid) // 2 + 1):
        repeat_part = myid[:length]
        num_parts = len(myid) // length
        if repeat_part * num_parts == myid:
            return True
def get_sum_silly(idrange):
    start, end = idrange.split('-')
    silly_sum = 0
    for myid in range(int(start), int(end) + 1):
        if if_silly(str(myid)):
            print(f"silly: {myid}")
            silly_sum += myid
    return silly_sum

print(sum(get_sum_silly(idrange) for idrange in ids))
