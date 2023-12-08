from itertools import cycle
from functools import reduce
instructions, network = [line.strip() for line in open("input.txt", "r").read().split('\n\n')]
instructions = [int(dir) for dir in instructions.replace('L', '0').replace('R', '1')]
network = {line.split(' = ')[0]: (line.split('(')[1][:3], line.split(', ')[1][:3]) for line in network.split('\n')}
start_nodes = [node for node in network.keys() if node[-1] == 'A']
node_counts = [[] for _ in start_nodes]
for node_ix, cur_node in enumerate(start_nodes):
    visited = set()
    for count, dir in enumerate(cycle(instructions)):
        if cur_node[-1] == 'Z':
            if ((count % len(instructions), cur_node) in visited):
                break
            visited.add((count % len(instructions), cur_node))
            node_counts[node_ix].append(count)
        cur_node = network[cur_node][dir]
print(reduce(lambda x, y: x * y, [node_count[0] // len(instructions) for node_count in node_counts]) * len(instructions))
