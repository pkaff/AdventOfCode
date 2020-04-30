import networkx as nx

input = open("input.txt", "r").read()[1:-1]
graph = nx.Graph()

pos = 0
groups = []
start = 0
ends = set()

for c in input:
    if c in 'NEWS':
        dir = {'N': 1j, 'W': -1, 'E': 1, 'S': -1j}[c]
        graph.add_edge(pos, pos + dir)
        pos = pos + dir
    elif c == '|':
        ends.add(pos)
        pos = start
    elif c == '(':
        groups.append((start, ends))
        start = pos
        ends = set()
    elif c == ')':
        start, ends = groups.pop()
        ends.add(pos)

lengths = nx.algorithms.shortest_path_length(graph, 0)

print(max(lengths.values()))
print(len([len for len in lengths.values() if len >= 1000]))