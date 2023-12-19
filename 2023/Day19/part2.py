from functools import reduce
from collections import defaultdict
parse_workflows, _ = list(map(lambda l: l.split('\n'), open("input.txt", "r").read().split('\n\n')))
workflows = defaultdict(lambda: [])
for workflow in parse_workflows:
    name, conditions = workflow.replace('}','').split('{')
    for condition in conditions.split(',')[:-1]:
        cond, next = condition.split(':')
        op = ''
        lt_ix = condition.find('<')
        if lt_ix != -1:
            var = cond[:lt_ix]
            val = int(cond[lt_ix + 1:])
            op = '<'
        else:
            gt_ix = condition.find('>')
            var = cond[:gt_ix]
            val = int(cond[gt_ix + 1:])
            op = '>'
        workflows[name].append(((var, op, val), next))
    workflows[name].append((tuple(), conditions.split(',')[-1]))

to_visit = [('in', {'x': range(1, 4001), 'm': range(1, 4001), 'a': range(1, 4001), 's': range(1, 4001)})]
result = 0
while to_visit:
    next, ranges = to_visit.pop()
    if next == 'A':
        result += reduce(lambda x, y: x * y, map(len, ranges.values()))
        continue

    prev_range = ranges.copy()
    for condition, neighbour in workflows[next]:
        ranges_copy = prev_range.copy()
        if condition:
            var, op, val = condition
            if op == '<':
                ranges_copy[var] = range(prev_range[var].start, min(prev_range[var].stop, val))
                prev_range[var] = range(max(prev_range[var].start, val), prev_range[var].stop)
            if op == '>':
                ranges_copy[var] = range(max(prev_range[var].start, val + 1), prev_range[var].stop)
                prev_range[var] = range(prev_range[var].start, min(prev_range[var].stop, val + 1))
        to_visit.append((neighbour, ranges_copy))

print(result)