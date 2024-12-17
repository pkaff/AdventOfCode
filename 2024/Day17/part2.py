def run_program(a):
    b = 0
    c = 0
    output = []
    while a != 0:
        #2,4
        b = a % 8 # [0, 7] low 3 bits relevant
        #1,5
        b ^= 5 # XOR 101 keeps bit 2, b = 010
        #7,5
        c = a//(2**b) # shift a 2 steps if next last bit is set, else keep a
        #1,6
        b ^= 6 # XOR 100 if bit 2 is set, else XOR 110
        #0,3
        a = a//(2**3) # shift 3 bits
        #4,0
        b ^= c # toggle bit 3 in a shifted 2 steps if next last bit is set, else toggle bit 2 and 3
        #5,5
        output.append(b%8) # output 3 least sig bits
        #3,0 = loop
    return output
target_output = [2,4,1,5,7,5,1,6,0,3,4,0,5,5,3,0]
to_try = [(0, -1)]
possible_vals = []
while to_try:
    val, offset = to_try.pop()
    for i in range(8):
        next_val = (val << 3) + i
        output = run_program(next_val)
        if output == target_output:
            possible_vals.append(next_val)
        elif output == target_output[offset:]:
            to_try.append((next_val, offset - 1))
print(min(possible_vals))