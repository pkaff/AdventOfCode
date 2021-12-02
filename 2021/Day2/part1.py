myin = [l.replace('\n', '') for l in list(open("input.txt", "r").readlines())]
horizontal = sum(int(l.split()[1]) if 'forward' in l else 0 for l in myin)
depth = sum(int(l.split()[1]) if 'down' in l else -int(l.split()[1]) if 'up' in l else 0 for l in myin)
print(depth*horizontal)
