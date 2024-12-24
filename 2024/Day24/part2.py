registers, gates = open("input.txt", "r").read().split('\n\n')
registers = {line.split(': ')[0]: int(line.split(': ')[1]) for line in registers.split('\n')}
gates = [line.split() for line in gates.split('\n')]
z_regs = sorted([outgate for _, _, _, _, outgate in gates if outgate[0] == 'z'], key=lambda x:int(x[1:]), reverse=True)
def str_to_op(op):
    if op == 'AND':
        return '&'
    if op == 'OR':
        return '|'
    if op == 'XOR':
        return '^'

wrong = set()
# Addition requires each bit to be XOR by bits at corresponding index and potential carry-over
for r1, op, r2, _, out_reg in gates:
    if out_reg[0] == 'z' and op != 'XOR' and out_reg != 'z45':
        wrong.add(out_reg)
    if op == 'XOR' and all([reg[0] not in ['x', 'y', 'z'] for reg in [r1, r2, out_reg]]):
        wrong.add(out_reg)
    if op == 'AND' and 'x00' not in [r1, r2]:
        for or1, oop, or2, _, oout_reg in gates:
            if (out_reg == or1 or out_reg == or2) and oop != 'OR':
                wrong.add(out_reg)
    if op == 'XOR':
        for or1, oop, or2, _, oout_reg in gates:
            if (out_reg == or1 or out_reg == or2) and oop == 'OR':
                wrong.add(out_reg)
print(','.join(sorted(wrong)))