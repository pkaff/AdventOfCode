from collections import defaultdict
import functools
import itertools
import sys
input = [line.strip('\n').split('; ') for line in open("input.txt", "r").readlines()]
flow_rates = dict()
dists = defaultdict(lambda: sys.maxsize)
nodes = set()
for line in input:
    label = line[0].split("Valve ")[1][:2]
    nodes.add(label)
    flow_rate = int(line[0].split('=')[1])
    if flow_rate != 0:
        flow_rates[label] = flow_rate
    connected_tunnels = [tunnel.strip(',') for tunnel in line[1].split()[4:]]
    for tunnel in connected_tunnels:
        dists[tunnel, label] = 1

#floyd-warshall for min distances
for k, i, j in itertools.product(nodes, nodes, nodes):
    dists[i, j] = min(dists[i, j], dists[i, k] + dists[k, j])

@functools.lru_cache(maxsize=None)
def tunnel_recursion(time_left, pos, to_visit, first):
    flows = []
    for neighbour in to_visit:
        if dists[pos, neighbour] >= time_left:
            continue
        next_time = time_left - dists[pos, neighbour] - 1
        added_flow = flow_rates[neighbour] * next_time
        flows.append(added_flow + tunnel_recursion(next_time, neighbour, to_visit-{neighbour}, first))
    flows.append(tunnel_recursion(26, 'AA', to_visit, False) if first else 0)
    return max(flows)

print(tunnel_recursion(26, 'AA', frozenset(flow_rates), True))
