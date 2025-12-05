input = [line.strip() for line in open("input.txt", "r").readlines()]
sizeX = len(input[0].strip())
sizeY = len(input)
rolls = {(x, y): True for y, row in enumerate(input) for x, char in enumerate(row) if char == '@'}
accessible = 0
for x, y in rolls:
    neighbours = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            nx, ny = x + dx, y + dy
            if 0 <= nx < sizeX and 0 <= ny < sizeY and (nx, ny) in rolls:
                neighbours += 1
    if neighbours < 4:
        accessible += 1
print(accessible)