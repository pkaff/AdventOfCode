graph, commands = open("input.txt", "r").read().split('\n\n')
graph = graph.split('\n')[:-1]
num_columns = len(graph[-1].split())
stacks = [[] for _ in  range(9)]
for line in reversed(graph):
    for col in range(num_columns):
        letter = line[col + 1 + col*3]
        if letter != ' ':
            stacks[col].append(letter)
for command in commands.split('\n'):
    command = command.split()
    num = int(command[1])
    from_col = int(command[3]) - 1
    to_col = int(command[5]) - 1
    if num > len(stacks[from_col]):
        num = len(stacks[from_col])
    stacks[to_col] += stacks[from_col][-num:]
    stacks[from_col] = stacks[from_col][:-num]
print(''.join([stack[-1] for stack in stacks if stack]))
