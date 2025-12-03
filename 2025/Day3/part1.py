batteries = [list(map(int, line.strip())) for line in open("input.txt", "r").readlines()]
joltage = 0
for battery in batteries:
    index_max = max(range(len(battery[:-1])), key=battery.__getitem__)
    sub_battery = battery[index_max + 1:]
    sub_index_max = max(range(len(sub_battery)), key=sub_battery.__getitem__)
    joltage += int(str(battery[index_max]) + str(sub_battery[sub_index_max]))
print(joltage)