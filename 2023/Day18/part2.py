instructions = [row.strip().replace('#', '0x').replace(')','').replace('(','').split()[-1] for row in open("input.txt", "r").readlines()]
instructions = [(complex(instruction[-1].replace('1', '1j').replace('0', '1').replace('2', '-1').replace('3', '-1j')), int(instruction[:-1], 16)) for instruction in instructions]
start = 0j
corners = [start]
for dir, steps in instructions:
    diff = dir * steps
    end = start + diff
    start = end
    corners.append(end)

area = 0
# Shoelace formula
for c1, c2 in zip(corners[:-1], corners[1:]):
    area += (c1.real * c2.imag) - (c1.imag * c2.real)
area *= 0.5

border_count = sum([int(abs(c1 - c2)) for c1, c2 in zip(corners[:-1], corners[1:])])

# Pick's theorem
# A = i + b/2 - 1, where i and b are the number of interior and boundary points respectively
interior_count = area - border_count/2 + 1

print(int(interior_count) + border_count)