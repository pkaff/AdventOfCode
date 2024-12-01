res = [line.split('   ') for line in open("input.txt", "r").readlines()]
left = sorted([int(entry[0]) for entry in res])
right = sorted([int(entry[1]) for entry in res])
print(sum(map(lambda x: abs(x[0] - x[1]), zip(left, right))))
