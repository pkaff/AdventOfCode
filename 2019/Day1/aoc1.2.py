inputs = [int(x) for x in open("input.txt", "r").readlines()]
fuel = 0
while any(i > 0 for i in inputs):
    inputs = [0 if x/3 - 2 < 0 else x/3 - 2 for x in inputs]
    fuel += sum(inputs)
print(fuel)