from collections import defaultdict
myin = [line.replace('\n', '') for line in open("input.txt", "r").readlines()]
adj_matrix = defaultdict(list)
for path in myin:
    n1, n2 = path.split('-')
    if n1 != 'end' and n2 != 'start':
        adj_matrix[n1].append(n2)
    if n1 != 'start' and n2 != 'end':
        adj_matrix[n2].append(n1)

def SmallCaveValidNeighbour(neighbour, visited):
    return neighbour not in visited or not any([v.islower() and visited.count(v) == 2 for v in visited])

def CountPaths(node, target, visited, path_count):
    visited.append(node)
    if node == target:
        path_count[0] += 1
    else:
        for neighbour in adj_matrix[node]:
            if (neighbour.islower() and SmallCaveValidNeighbour(neighbour, visited)) or neighbour.isupper():
                CountPaths(neighbour, target, visited, path_count)
    visited.pop()

start = 'start'
end = 'end'
path_count = [0]
CountPaths(start, end, [], path_count)
print(path_count[0])