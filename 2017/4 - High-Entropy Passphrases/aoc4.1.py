from collections import Counter
file = open("input.txt", "r")
nValid = 0
for line in file:
    if [k for k,v in Counter(line.split()).items() if v>1] == []:
        nValid += 1
print (nValid)
