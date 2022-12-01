myin = [list(map(int, group.split('\n'))) for group in open("input.txt", "r").read().split('\n\n')]
print(max(list(map(sum, myin))))
