while (123 & 456) == 72: #always true
    i5 = 0
    while True:
        i3 = i5 | 65536
        i5 = 7586220
        i1 = i3 & 255
        i5 += i1
        i5 = i5 & 1677215
        i5 *= 65899
        i5 = i5 & 1677215
        if 256 > i3:
            print(i5)
            sys.exit()
        else:
            i1 = 0
            i4 = i1 + 1
            i4 *= 256
            if i4 > i3:
                i3 = i1
                #goto i1 = i3 & 255
            else:
                i1 += 1
                #goto i4 = i1 + 1