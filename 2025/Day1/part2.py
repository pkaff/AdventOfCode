res = list(map(lambda x: int(x[1:]) if x[0] == 'R' else -int(x[1:]), [line.strip() for line in open("input.txt", "r").readlines()]))
cur = 50
count = 0
for x in res:
    if cur == 0 or (cur + x >= 100):
        count += abs((cur + x)) // 100
    elif cur + x <= 0:
        count += 1 + abs((cur + x)) // 100
    cur = (cur + x) % 100
print(count)