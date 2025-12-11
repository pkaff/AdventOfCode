input = {line.split(':')[0]: line.split(':')[1].strip().split() for line in open("input.txt", "r").readlines()}
start = 'you'
end = 'out'
def DFS(target, visited):
    cur = visited[-1]
    if target == cur:
        return 1
    num_paths = 0
    for neighbour in input[cur]:
        num_paths += DFS(target, visited + (neighbour,))
    return num_paths
print(DFS(end, (start,)))
