import numpy as np
def allEqual(sums):
    if sums == []:
        return False
    return sums[1:] == sums[:-1]
def recursiveTraverse(my_dict, key):
    sum =  int(my_dict[key][0])
    for k in my_dict[key][1]:
        sum += recursiveTraverse(my_dict, k)
    return sum

def recursiveTraverse2(my_dict, key):
    if (my_dict[key][1] == []):
        return int(my_dict[key][0])
    else:
        sums = []
        for k in my_dict[key][1]:
            sums.append(recursiveTraverse2(my_dict, k))
        if not allEqual(sums):
            ix = -1
            for i in range(len(sums)-2):
                if sums[i] != sums[i+1] or sums[i] != sums[i+2]:
                    if sums[i] == sums[i+1]:
                        ix = i+2
                    else:
                        ix = i+1
                    break
            print(sums)
            print(my_dict[key][1][ix])
            print(int(my_dict[my_dict[key][1][ix]][0]) - (sums[ix] - sums[ix-1]))
        return sum(sums) + int(my_dict[key][0])
        
    
file = open("input.txt", "r")
towers = file.readlines()
my_dict = {}
for t in towers:
    tList = t.split()
    strippedList = []
    if len(tList) > 2:
        strippedList = [s.replace(",", "") for s in tList[3:]]
    my_dict[tList[0]] = [tList[1][1:-1], strippedList]
        
bottom = "azqje"
recursiveTraverse2(my_dict, bottom)

