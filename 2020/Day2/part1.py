#import re
#print(len([1 for parts in [re.split(' |:|-', s.rstrip()) for s in open("input.txt", "r").readlines()] if parts[4].count(parts[2]) >= int(parts[0]) if parts[4].count(parts[2]) <= int(parts[1])]))
myin = open("input.txt", "r").readlines()
numValid = 0
for s in myin:
    limits, letter, password = s.split()
    minLim, maxLim = list(map(int, limits.split('-')))
    letter = letter.replace(':', '')
    frequency = password.count(letter)
    if frequency >= minLim and frequency <= maxLim:
        numValid += 1
print(numValid)
