from heapq import nlargest

myin = [list(map(int, group.split('\n'))) for group in open("input.txt", "r").read().split('\n\n')]
print(sum(nlargest(3, list(map(sum, myin)))))
