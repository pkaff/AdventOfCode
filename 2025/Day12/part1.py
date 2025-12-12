input = [line.split('\n') for line in open("input.txt", "r").read().split('\n\n')]
presents = [''.join(present[1:]) for present in input[:-1]]
grids = [(list(map(int, grid.split(':')[0].split('x'))), list(map(int, grid.split(' ')[1:]))) for grid in input[-1]]
fits = 0
for (x, y), numpresents in grids:
    gridsize = x * y
    areatofit = sum(num * presents[presentix].count('#') for presentix, num in enumerate(numpresents))
    if areatofit <= gridsize:
        fits += 1    
print(fits)