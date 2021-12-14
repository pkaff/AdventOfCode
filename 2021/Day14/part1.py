from collections import Counter
template, myin = open("input.txt", "r").read().split('\n\n')
mymap = {entry[0]: entry[1] for entry in [line.split(' -> ') for line in myin.split('\n') if line]}
for step in range(10):
    for ix in reversed(range(len(template) - 1)):
        pair = template[ix:ix+2]
        if pair in mymap.keys():
            template = template[:ix + 1] + mymap[pair] + template[ix + 1:]
most_common = Counter(template).most_common()
print(most_common[0][1] - most_common[-1][1])
