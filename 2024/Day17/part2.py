from itertools import product
a = 24847151
b = 0
c = 0
output = [7,3,1,3,6,3,6,0,2]
#output = []
#0b1011110110010001100101111
a_bits = "1011110110010001100101111"
for res in output:
    for least_bits in product([0, 1], repeat=3):
        print(least_bits)

        print("a:", bin(a))
        #2,4
        b = a % 8 # [0, 7] low 3 bits relevant
        print("b:", bin(b))
        #1,5
        b ^= 5 # XOR 101 keeps bit 2, b = 010
        print("b:", bin(b))
        #7,5
        c = int(a/2**b) # shift a 2 steps if next last bit is set, else keep a
        print("c:", bin(c))
        #1,6
        b ^= 6 # XOR 110 keeps bit 3, b = 100
        print("b:", bin(b))
        #0,3
        a = int(a/2**3) # shift 3 bits
        print("a:", bin(a))
        #4,0
        b ^= c # toggle bit 3 in a shifted 2 steps if next last bit is set, else toggle bit 2 and 3
        print("b:", bin(b))
        #5,5
        print("out:", bin(b%8))
        output.append(str(b%8)) #output 3 least sig bits, 3 least sig bits must be same after each op
print(','.join(output))