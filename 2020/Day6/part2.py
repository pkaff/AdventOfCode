
from collections import Counter

declarations = [["", 0]]
myinput = [l.strip() for l in open("input.txt", "r").readlines()]
for line in myinput:
    if not line:
        declarations.append(["", 0])
    else:
        declarations[-1][1] += 1
        declarations[-1][0] += line
print(sum([1 if value == groupSize else 0 for questions, groupSize in declarations for value in Counter(questions).values()]))