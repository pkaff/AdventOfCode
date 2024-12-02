res = [list(map(int, line.split())) for line in open("input.txt", "r").readlines()]
def is_safe(diffs):
    return all([abs(diff) <=3 and abs(diff) >= 1 and diff*diffs[0] > 0 for diff in diffs])
count = 0
for lst in res:
    diffs = list(map(lambda x: x[0] - x[1], zip(lst[:-1], lst[1:])))
    if is_safe(diffs):
        count += 1
        continue
    for remove_ix in range(len(lst)):
        tmp_lst = lst[:remove_ix] + lst[remove_ix + 1:]
        diffs = list(map(lambda x: x[0] - x[1], zip(tmp_lst[:-1], tmp_lst[1:])))
        if is_safe(diffs):
            count += 1
            break
print(count)