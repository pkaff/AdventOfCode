from itertools import combinations
def manhattan_dist(cord1, cord2):
    return abs(cord1[0] - cord2[0]) + abs(cord1[1] - cord2[1])
universe = [line.strip() for line in open("input.txt", "r").readlines()]
empty_rows = [ix for ix, row in enumerate(universe) if '#' not in row]
empty_cols = [ix for ix, col in enumerate(zip(*universe)) if '#' not in col]
galaxies = [(x, y) for x, row in enumerate(universe) for y, c in enumerate(row) if c == '#']
dist = 0
for galaxy1, galaxy2 in combinations(galaxies, 2):
    n_empty_rows = sum([1 for empty_row in empty_rows if empty_row > min(galaxy1[0], galaxy2[0]) and empty_row < max(galaxy1[0], galaxy2[0])])
    n_empty_cols = sum([1 for empty_col in empty_cols if empty_col > min(galaxy1[1], galaxy2[1]) and empty_col < max(galaxy1[1], galaxy2[1])])
    dist += manhattan_dist(galaxy1, galaxy2) + 999999*n_empty_rows + 999999*n_empty_cols
print(dist)