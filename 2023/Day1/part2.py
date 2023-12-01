def get_num(line):
    nums = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}
    for txt in nums:
        index = line.find(txt)
        if index != -1:
            line = line[:index + len(txt) - 1] + nums[txt] + line[index + len(txt) - 1:]
        rindex = line.rfind(txt)
        if rindex != -1:
            line = line[:rindex + len(txt) - 1] + nums[txt] + line[rindex + len(txt) - 1:]
    digits = list(filter(str.isdigit, line))
    return int(digits[0] + digits[-1])

print(sum([get_num(line) for line in open("input.txt", "r").readlines()]))
