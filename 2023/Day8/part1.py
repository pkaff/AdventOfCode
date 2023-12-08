from itertools import cycle
instructions, network = [line.strip() for line in open("input.txt", "r").read().split('\n\n')]
instructions = [int(dir) for dir in instructions.replace('L', '0').replace('R', '1')]
network = {line.split(' = ')[0]: (line.split('(')[1][:3], line.split(', ')[1][:3]) for line in network.split('\n')}
cur_node = 'AAA'
for count, dir in enumerate(cycle(instructions)):
    if cur_node == 'ZZZ':
        print(count)
        exit()
    cur_node = network[cur_node][dir]