fishmap = [0] * 9
for fish in open("input.txt", "r").read().replace('\n', '').split(','):
    fishmap[int(fish)] += 1
for day in range(256):
    n_new = fishmap[0]
    fishmap = fishmap[1:]
    fishmap[6] += n_new
    fishmap.append(n_new)
print(sum(fishmap))
