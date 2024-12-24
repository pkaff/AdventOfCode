registers, gates = open("input.txt", "r").read().split('\n\n')
registers = {line.split(': ')[0]: line.split(': ')[1] for line in registers.split('\n')}
gates = [line.split() for line in gates.split('\n')]
z_regs = sorted([outgate for _, _, _, _, outgate in gates if outgate[0] == 'z'], key=lambda x:int(x[1:]), reverse=True)
graph = {}
for r1, op, r2, _, outreg in gates:
    assert((r1, op, r2) not in graph)
    graph[outreg] = (r1, op, r2)
def str_to_op(op):
    if op == 'AND':
        return '&'
    if op == 'OR':
        return '|'
    if op == 'XOR':
        return '^'
def transform_to_inreg(reg):
    if reg in registers:
        return registers[reg]
    r1, op, r2 = graph[reg]
    return "(" + transform_to_inreg(r1) + str_to_op(op) + transform_to_inreg(r2) + ")"
    
for ix, z_reg in enumerate(z_regs):
    z_regs[ix] = str(eval(transform_to_inreg(z_reg)))
print(int(''.join(z_regs), 2))