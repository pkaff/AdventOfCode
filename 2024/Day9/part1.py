input = [int(c) for c in open("input.txt", "r").read().strip()]
def get_next():
    from_left = True
    cur_left_val = 0
    cur_right_val = len(input)//2
    left_pos = 0
    right_pos = len(input) - 1
    while left_pos <= right_pos:
        if from_left:
            if input[left_pos] == 0:
                left_pos += 1
                cur_left_val += 1
                from_left = False
            else:
                yield cur_left_val
                input[left_pos] -= 1
        else:
            if input[left_pos] == 0:
                left_pos += 1
                from_left = True
            elif input[right_pos] == 0:
                right_pos -= 2
                cur_right_val -= 1
            else:
                yield cur_right_val
                input[left_pos] -= 1
                input[right_pos] -= 1
print(sum([ix*val for ix, val in enumerate(get_next())]))