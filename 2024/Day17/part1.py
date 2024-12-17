a = 24847151
b = 0
c = 0
output = []
while a != 0:
    #2,4
    b = a % 8
    #1,5
    b ^= 5
    #7,5
    c = int(a/2**b)
    #1,6
    b ^= 6
    #0,3
    a = int(a/2**3)
    #4,0
    b = b^c
    #5,5
    output.append(str(b%8))
    #3,0 = loop
print(','.join(output))