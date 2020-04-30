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

def makeKnotHash(str):    
    lengths = [ord(c) for c in str] + [17, 31, 73, 47, 23]
    sparseHash = [i for i in range(256)]
    skipSize = 0
    pos = 0
    for round in range(64):
        for l in lengths:
            if (l != 0):
                reverseElements(sparseHash, pos, pos + l)
            pos += l + skipSize
            if pos >= len(sparseHash):
                pos = pos % len(sparseHash)
            skipSize += 1
    denseHash = [0 for i in range(16)]
    for block in range(16):
        xored = 0
        for h in sparseHash[16*block:(block+1)*16]:
            xored = xored ^ h
        denseHash[block] = xored
    return ''.join(list(map(lambda x: format(x, 'x').zfill(2), denseHash)))
