import intervaltree
ranges, _ = open("input.txt", "r").read().split('\n\n')
ranges = [[int(start), int(end)] for start, end in (line.split('-') for line in ranges.splitlines())]
tree = intervaltree.IntervalTree.from_tuples([[start, end] for start, end in ranges if start != end])
single_ranges = [int(r[0]) for r in ranges if r[0] == r[1]]
tree.merge_overlaps()
print(sum(interval.end - interval.begin + 1 for interval in tree.items()) + sum(1 if any(r.overlaps(id) for r in tree) else 0 for id in single_ranges))
