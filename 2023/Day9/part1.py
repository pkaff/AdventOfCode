scans = [list(map(int, line.strip().split())) for line in open("input.txt", "r").readlines()]
predictions = []
for scan in scans:
    lasts = [scan[-1]]
    while not all(v == 0 for v in scan):
        scan = [y - x for x, y in zip(scan[:-1], scan[1:])]
        lasts.append(scan[-1])
    predictions.append(sum(lasts))
print(sum(predictions))
