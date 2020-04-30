def is_prime(a):
    return all(a % i for i in range(2, a))
b = 109300
c = 126300
h = 0
i = b
while i <= c:
    if not is_prime(i):
        h += 1
    i += 17
print(h)