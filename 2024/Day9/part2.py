input = [(None if ix % 2 != 0 else ix // 2, int(c)) for ix, c in enumerate(open("input.txt", "r").read().strip())]
for rpos in range(len(input) - 1, -1, -1):
    for lpos in range(rpos):
        r_val, r_count = input[rpos]
        l_val, l_count = input[lpos]

        if l_val == None and r_val != None and l_count >= r_count:
            input[rpos] = (None, r_count)
            input[lpos] = (None, l_count - r_count)
            input.insert(lpos, (r_val, r_count))
flatten = lambda xss: [x for xs in xss for x in xs]
lists_of_vals = [[val if val else 0]*num for val, num in input]
print(sum([val*ix for ix, val in enumerate(flatten(lists_of_vals)) if val]))