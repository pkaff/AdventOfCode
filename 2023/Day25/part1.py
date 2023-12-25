from networkx import Graph, minimum_cut
from itertools import combinations
input = [line.strip() for line in open("input.txt", "r").readlines()]
graph = Graph()
for line in input:
    node, neighbours = line.split(': ')
    for neighbour in neighbours.split(' '):
        graph.add_edge(node, neighbour, capacity=1)

for n1, n2 in combinations(graph.nodes, 2):
    cut, partition = minimum_cut(graph, n1, n2)
    if cut == 3:
        print(len(partition[0])*len(partition[1]))
        break