def recurse_lst(lst):
    if len(lst) == 2:
        return lst[0] - lst[1]
    return lst[0] - recurse_lst(lst[1:])
scans = [list(map(int, line.strip().split())) for line in open("input.txt", "r").readlines()]
predictions = []
for scan in scans:
    firsts = [scan[0]]
    while not all(v == 0 for v in scan):
        scan = [y - x for x, y in zip(scan[:-1], scan[1:])]
        firsts.append(scan[0])
    predictions.append(recurse_lst(firsts))
print(sum(predictions))
