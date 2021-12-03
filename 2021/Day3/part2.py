binaries = [l.replace('\n', '') for l in list(open("input.txt", "r").readlines())]
ix = 0
oxGenRating = binaries[:]
while len(oxGenRating) > 1:
    ixthBits = list(zip(*oxGenRating))[ix]
    mostCommonBit = '1' if ixthBits.count('1') >= ixthBits.count('0') else '0'
    oxGenRating = [l for l in oxGenRating if l[ix] == mostCommonBit]
    ix += 1

ix = 0
co2ScrubRating = binaries[:]
while len(co2ScrubRating) > 1:
    ixthBits = list(zip(*co2ScrubRating))[ix]
    leastCommonBit = '1' if ixthBits.count('1') < ixthBits.count('0') else '0'
    co2ScrubRating = [l for l in co2ScrubRating if l[ix] == leastCommonBit]
    ix += 1

print(int(co2ScrubRating[0], 2) * int(oxGenRating[0], 2))
