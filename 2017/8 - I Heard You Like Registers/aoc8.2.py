def parseCond(my_dict, r, op, n, cond, maximum):
    if r not in my_dict:
        my_dict[r] = 0
    if cond[0] not in my_dict:
        my_dict[cond[0]] = 0
    if eval(str(my_dict[cond[0]]) + " " + cond[1] + " " + cond[2]):
        if op == "inc":
            my_dict[r] += int(n)
        elif op == "dec":
            my_dict[r] -= int(n)
    return max(maximum, my_dict[r])
file = open("input.txt", "r")
instructions = file.readlines()
my_dict = {}
maximum = 0
for i in instructions:
    r, op, n, cond = [i.split()[0], i.split()[1], i.split()[2], i.split()[4:]]
    maximum = parseCond(my_dict, r, op, n, cond, maximum)
print(maximum)
