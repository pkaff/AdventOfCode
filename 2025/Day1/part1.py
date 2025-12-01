res = list(map(lambda x: int(x[1:]) if x[0] == 'R' else -int(x[1:]), [line.strip() for line in open("input.txt", "r").readlines()]))
cur = 50
count = 0
for x in res:
    cur = (cur + x) % 100
    if cur == 0:
        count += 1
print(count)