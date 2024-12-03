import re
input = ("do()" + open("input.txt", "r").read()).replace('\n', '').split("don't()")
res = 0
for line in input:
    dos = line.split("do()")
    for to_mul in dos[1:]:
        digits = list(map(lambda t: int(t[0]) * int(t[1]), re.findall(r"mul\((\d+),(\d+)\)", to_mul)))
        res += sum(digits)
print(res)