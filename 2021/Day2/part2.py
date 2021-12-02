myin = [l.replace('\n', '') for l in list(open("input.txt", "r").readlines())]
horizontal = 0
depth = 0
aim = 0
for line in myin:
    val = int(line.split()[1])
    if 'forward' in line:
        horizontal += val
        depth += val*aim
    elif 'up' in line:
        aim -= val
    elif 'down' in line:
        aim += val
print(horizontal*depth)
