from collections import defaultdict
inputs = [line.strip().split('-') for line in open("input.txt", "r").readlines()]
connections = defaultdict(set)
for c1, c2 in inputs:
    connections[c1].add(c2)
    connections[c2].add(c1)

def find_largest_set(cur_computers, remaining):
    if len(remaining) == 0:
        return cur_computers
    while remaining:
        other_computer = remaining.pop()
        if all(other_computer in connections[computer] or computer in connections[other_computer] for computer in cur_computers):
            cur_computers |= {other_computer}
        return find_largest_set(cur_computers, remaining)

best_set = set()
for computer in set(connections.keys()):
    largest = find_largest_set({computer}, set(connections.keys()) - {computer})
    if len(largest) > len(best_set):
        best_set = largest
print(','.join(sorted(best_set)))