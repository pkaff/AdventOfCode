ops = [line.strip() for line in open("input.txt", "r").readlines()]
cycle = 1
regx = 1
signal_strength = 0
for op in ops:
    if cycle % 40 == 20:
        signal_strength += regx * cycle
    if op == 'noop':
        cycle += 1
    else:
        cycle += 1
        if cycle % 40 == 20:
            signal_strength += regx * cycle
        cycle += 1
        regx += int(op.split()[1])
print(signal_strength)