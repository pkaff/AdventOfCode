nums = [[-2 if c == '=' else -1 if c == '-' else int(c) for c in line.strip('\n')] for line in open("input.txt", "r").readlines()]
def snafu_to_base_10(lst):
    tot = 0
    for place, dig in enumerate(reversed(lst)):
        tot += pow(5, place) * dig
    return tot
def base_10_to_snafu(num):
    if num == 0:
        return 0
    digits = []
    while num:
        digits.append(str(num % 5))
        num = num // 5

    for ix, d in enumerate(digits):
        carry = False
        if d == '3':
            digits[ix] = '='
            carry = True
        elif d == '4':
            digits[ix] = '-'
            carry = True
        elif d == '5':
            digits[ix] = '0'
            carry = True
        if carry:
            if ix == len(digits) - 1:
                digits.append('1')
            else:
                digits[ix + 1] = str(int(digits[ix + 1]) + 1)
    return ''.join(list(reversed(digits)))

base_10_sum = sum(map(snafu_to_base_10, nums))
print(base_10_to_snafu(base_10_sum))