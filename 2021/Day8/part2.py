myin = [line.replace('\n', '').split(' | ') for line in open("input.txt", "r").readlines()]
length_map = {2: [1], 5: [2, 3, 5], 6: [0, 6, 9],  3: [7], 4: [4], 7: [8]}
res = 0
for line in myin:
    inputs_known = list(map(set, [chars for chars in line[0].split() if len(length_map[len(chars)]) == 1]))
    inputs_unknown = list(map(set, [chars for chars in line[0].split() if len(length_map[len(chars)]) == 3]))
    outputs = list(map(set, line[1].split()))
    nums = [set()]*10
    for chars in inputs_known:
        nums[length_map[len(chars)][0]] = chars
    for chars in inputs_unknown:
        if len(chars) == 5:
            #2, 3 or 5
            if len(chars - nums[4]) == 3:
                nums[2] = chars
            elif len(chars - nums[1]) == 3:
                nums[3] = chars
            else:
                nums[5] = chars
        elif len(chars) == 6:
            #0, 6 or 9
            if len(chars - nums[4]) == 2:
                nums[9] = chars
            elif len(chars - nums[1]) == 4:
                nums[0] = chars
            else:
                nums[6] = chars
    res += int(''.join([str(nums.index(charset)) for charset in outputs]))
print(res)
