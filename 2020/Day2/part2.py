#import re
#print(len([1 for parts in [re.split(' |:|-', s.rstrip()) for s in open("input.txt", "r").readlines()] if (parts[4][int(parts[0]) - 1] == parts[2]) != (parts[4][int(parts[1]) - 1] == parts[2])]))
myin = open("input.txt", "r").readlines()
numValid = 0
for s in myin:
    limits, letter, password = s.split()
    pos1, pos2 = list(map(int, limits.split('-')))
    letter = letter.replace(':', '')
    if (password[pos1 - 1] == letter) != (password[pos2 - 1] == letter):
        numValid += 1
print(numValid)
