import re

file = open("input.txt", "r")
groups = file.read()
groups = re.sub(r'!.', r'', groups)
groups = re.findall(r'<(.*?)>', groups)
nGarbage = 0
for g in groups:
    nGarbage += len(g)
print(nGarbage)