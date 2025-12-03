batteries = [list(map(int, line.strip())) for line in open("input.txt", "r").readlines()]
joltage = 0
for battery in batteries:
    battery_str = ''
    index_max = 0
    for k in range(12):
        index_max = max(range(index_max, len(battery) - (12 - k - 1)), key=battery.__getitem__)
        battery_str += str(battery[index_max])
        index_max += 1
    joltage += int(battery_str)
print(joltage)