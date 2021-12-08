myin = [line.replace('\n', '').split(' | ') for line in open("input.txt", "r").readlines()]
outputs = [line[1] for line in myin]
unique_lengths = [2, 3, 4, 7]
print(sum([1 if len(wire) in unique_lengths else 0 for output in outputs for wire in output.split()]))
