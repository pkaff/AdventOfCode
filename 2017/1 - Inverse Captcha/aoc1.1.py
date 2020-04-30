import sys
input = sys.argv[1]
zipped = zip(input, input[1:] + input[:1])
sum = 0
for p, p2 in zipped:
    if p == p2:
       sum += int(p)
    
print(sum)