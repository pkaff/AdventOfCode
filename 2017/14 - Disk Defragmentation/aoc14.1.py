from knothash import makeKnotHash
knothashes = [makeKnotHash("hfdlxzhv" + "-" + str(i)) for i in range(128)]
binaryhashes = []
for k in knothashes:
    binaryhashes.append(''.join(list(map(lambda x: bin(int(x, 16))[2:].zfill(4), k))))
print(sum(b.count("1") for b in binaryhashes))