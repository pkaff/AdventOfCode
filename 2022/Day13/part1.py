myin = [list(map(eval, packets.split('\n'))) for packets in open("input.txt", "r").read().split('\n\n')]
def compare(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return -1
        if left > right:
            return 1
        if left == right:
            return 0
    if type(left) == list and type(right) == list:
        minLen = min(len(left), len(right))
        for ix in range(minLen):
            ret = compare(left[ix], right[ix])
            if ret == -1 or ret == 1:
                return ret
        if len(left) < len(right):
            return -1
        if len(left) > len(right):
            return 1
        if len(left) == len(right):
            return 0
    if type(left) == int:
        return compare([left], right)
    if type(right) == int:
        return compare(left, [right])

ixs = []
for ix, (left, right) in enumerate(myin):
    if compare(left, right) == -1:
        ixs.append(ix + 1)
print(sum(ixs))
