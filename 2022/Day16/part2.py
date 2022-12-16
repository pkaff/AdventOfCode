from collections import defaultdict
import functools
input = [line.strip('\n').split('; ') for line in open("input.txt", "r").readlines()]
flow_rates = defaultdict(int)
adj_list = defaultdict(list)
for line in input:
    label = line[0].split("Valve ")[1][:2]
    flow_rate = int(line[0].split('=')[1])
    flow_rates[label] = flow_rate
    connected_tunnels = [tunnel.strip(',') for tunnel in line[1].split()[4:]]
    for tunnel in connected_tunnels:
        adj_list[label].append(tunnel)

print(flow_rates)
print(adj_list)

@functools.lru_cache(maxsize=None)
def tunnel_recursion(pos, time_left, opened):
    if time_left <= 0:
        return 0
    mypos, elepos = pos
    max_flow = 0
    added_flow = 0
    if pos not in opened:
        added_flow = flow_rates[pos] * (time_left - 1)
        new_opened = opened + (pos,)
    for neighbour in adj_list[pos]:
        if added_flow != 0:
            max_flow = max(max_flow, added_flow + tunnel_recursion(neighbour, time_left - 2, new_opened))
        max_flow = max(max_flow, tunnel_recursion(neighbour, time_left - 1, opened))
    return max_flow

print(tunnel_recursion(('AA', 'AA'), 26, tuple()))