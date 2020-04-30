import re

file = open("input.txt", "r")
groups = file.read()
groups = re.sub(r'!.', r'', groups)
groups = re.sub(r'<(.*?)>', r'', groups)
score = 0
total = 0
for c in groups:
    if c == '{':
        score += 1
    elif c == ',':
        continue
    elif c == '}':
        total += score
        score -= 1
print (total)