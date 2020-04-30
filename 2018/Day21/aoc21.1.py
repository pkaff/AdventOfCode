import sys

i5 = 0
while True:
    i3 = i5 | 65536
    i5 = 7586220
    while True:
        i1 = i3 & 255
        i5 += i1
        i5 = i5 & 16777215
        i5 *= 65899
        i5 = i5 & 16777215
        if 256 > i3:
            print(i5)
            sys.exit()
        else:
            i1 = 0
            while True:
                i4 = i1 + 1
                i4 *= 256
                if i4 > i3:
                    break
                i1 += 1
            i3 = i1

