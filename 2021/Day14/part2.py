from math import ceil
from collections import Counter
from collections import defaultdict
template, myin = open("input.txt", "r").read().split('\n\n')
mymap = {entry[0]: entry[1] for entry in [line.split(' -> ') for line in myin.split('\n') if line]}
template_freq = defaultdict(int)
for ix, _ in enumerate(template[:-1]):
    template_freq[template[ix:ix+2]] += 1
for step in range(40):
    template_freq_copy = template_freq.copy()
    for key, val in template_freq_copy.items():
        if val != 0 and key in mymap.keys():
            template_freq[key] -= val
            template_freq[key[0] + mymap[key]] += val
            template_freq[mymap[key] + key[1]] += val
letter_freq = defaultdict(int)
for key, value in template_freq.items():
    letter_freq[key[0]] += value
    letter_freq[key[1]] += value
letter_freq = list(map(lambda pair: ceil(pair[1]/2), letter_freq.items()))
print(max(letter_freq) - min(letter_freq))
