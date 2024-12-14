inputs = [line.strip().split() for line in open("input.txt", "r").readlines()]
inputs = [(list(map(int, line[0][2:].split(','))), list(map(int, line[1][2:].split(',')))) for line in inputs]
width = 101
height = 103
def print_grid(positions):
    for y in range(height):
        str = ''
        for x in range(width):
            if (x, y) in positions:
                str += 'X'
            else:
                str += '.'
        print(str)

for iteration in range(10000):
    positions = set(((pos[0] + vel[0]*iteration) % width, (pos[1] + vel[1]*iteration) % height) for pos, vel in inputs)
    print("Grid at iteration", iteration)
    print_grid(positions)
