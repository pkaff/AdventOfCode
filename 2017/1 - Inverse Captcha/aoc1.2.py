import sys
input = sys.argv[1]
zipped = zip(input, input[int(len(input)/2):] + input[:int(len(input)/2)])
sum = 0
for p, p2 in zipped:
    if p == p2:
       sum += int(p)
    
print(sum)