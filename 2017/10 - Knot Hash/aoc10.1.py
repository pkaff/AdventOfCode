def reverseElements(lst, start, end):
    nReverse = end - start
    if end >= len(lst):
        nList = lst[start:] + lst[:end % len(lst)]
        nList = nList[::-1]
        lst[start:] = nList[:len(lst[start:])]
        nReverse -= len(lst) - 1 - start
        lst[:end % len(lst)] = nList[len(lst[start:]):]
    else:
        lst[start:end] = lst[start:end][::-1]
    return lst
    
file = open("input.txt", "r")
lengths = list(map(int, file.read().split(",")))
lst = [i for i in range(256)]
skipSize = 0
pos = 0
for l in lengths:
    if (l != 0):
        reverseElements(lst, pos, pos + l)
    pos += l + skipSize
    if pos >= len(lst):
        pos = pos % len(lst)
    skipSize += 1
print(lst[0]*lst[1])