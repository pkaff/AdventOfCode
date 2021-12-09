myin = {(x, y): int(c) for (y, line) in enumerate(open("input.txt", "r").readlines()) for (x, c) in enumerate(line.replace('\n', ''))}
maxX = max([x for (x, y) in myin.keys()])
maxY = max([y for (x, y) in myin.keys()])
def get_neighbour_values(x, y):
    indices = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
    neighbour_values = []
    for (xx, yy) in indices:
        if xx >= 0 and xx <= maxX and yy >= 0 and yy <= maxY:
            neighbour_values.append(myin[(xx, yy)])
    return neighbour_values
risk_level = 0
for ((x, y), height) in myin.items():
    neighbour_values = get_neighbour_values(x, y)
    if height < min(neighbour_values):
        risk_level += height + 1
print(risk_level)
