import re
input = open("input.txt", "r").read().replace('\n', '')
digits = list(map(lambda t: int(t[0]) * int(t[1]), re.findall(r"mul\((\d+),(\d+)\)", input)))
print(sum(digits))