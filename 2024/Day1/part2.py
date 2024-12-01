from collections import Counter

res = [line.split('   ') for line in open("input.txt", "r").readlines()]
left = [int(entry[0]) for entry in res]
right = Counter([int(entry[1]) for entry in res])
print(sum([lentry*right[lentry] for lentry in left]))
