def recursiveTraverse(my_dict, key, seenKeys):
    for k in my_dict[key]:
        if k in seenKeys:
            continue
        seenKeys.add(k)
        recursiveTraverse(my_dict, k, seenKeys)

file = open("input.txt", "r")
towers = file.readlines()
my_dict = {}
for t in towers:
    tList = t.split()
    if len(tList) <= 2:
        my_dict[tList[0]] = []
    else:
        strippedList = [s.replace(",", "") for s in tList[3:]]
        if tList[2] == '->':
            my_dict[tList[0]] = strippedList
        
seenKeys = set()
for k, v in my_dict.items():
    recursiveTraverse(my_dict, k, seenKeys)

for k, v in my_dict.items():
    if k not in seenKeys:
        print(k)
        break