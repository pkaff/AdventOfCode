a = 24847151
print(bin(a))
b = 0
c = 0
output = [7,3,1,3,6,3,6,0,2]
#0b1011110110010001100101111
bits = 0b1011110110010001100101111
for res in output:
    #2,4
    b = a % 8 # [0, 7] low 3 bits relevant
    print(bin(b))
    #1,5
    b ^= 5 # XOR 101 keeps bit 2, b = 010
    print(bin(b))
    #7,5
    c = int(a/2**b) # shift a 2 steps if next last bit is set
    print(bin(c))
    #1,6
    print(bin(b))
    b ^= 6 # XOR 110 keeps bit 3, b = 100
    print(bin(b))
    #0,3
    a = int(a/2**3) # shift 3 bits
    #4,0
    b ^= c # toggle bit 3 in a shifted 2 steps if next last bit is set
    print(bin(b))
    #5,5
    exit()
    output.append(str(b%8)) #output 3 least sig bits, 3 least sig bits must be same after each op
    #3,0 = loop
print(','.join(output))