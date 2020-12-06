
from collections import Counter
declarations = [("".join(l.split("\n")), len(l.split("\n"))) for l in open("input.txt", "r").read().split("\n\n")]
print(sum([1 if value == groupSize else 0 for questions, groupSize in declarations for value in Counter(questions).values()]))