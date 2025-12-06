input = [line.strip('\n') for line in open("input.txt", "r").readlines()]
total = 0
curop = ''
nums = list(map(list, zip(*input[:-1])))
for col, maybeop in enumerate(input[-1]):
    if maybeop in ['*', '+']:
        curop = maybeop
        cur_total = 0 if curop == '+' else 1
    if all([c == ' ' for c in nums[col]]):
        total += cur_total
    else:
        num = int(''.join(nums[col]))
        if curop == '*':
            cur_total *= num
        elif curop == '+':
            cur_total += num
total += cur_total
print(total)