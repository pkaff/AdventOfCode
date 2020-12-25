def transform(subject, pubKey):
    val = 1
    ix = 0
    while val != pubKey:
        val *= subject
        val %= 20201227
        ix += 1
    return ix, val
pub1, pub2 = [int(l.rstrip()) for l in open("input.txt").readlines()]
ix1, val1 = transform(7, pub1)
ix2, val2 = transform(7, pub2)
val = 1
for ix in range(ix2):
    val = (val * pub1) % 20201227
print(val)