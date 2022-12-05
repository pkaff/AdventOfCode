myin = [[set(range(int(startstop[0]), int(startstop[1]) + 1)) for startstop in [idrange.split('-') for idrange in line.strip().split(',')]] for line in open("input.txt", "r").readlines()]
print(sum([1 for elf1, elf2 in myin if elf1.intersection(elf2)]))
