def draw(crt, cycle, pos):
    draw_pos = (cycle - 1) % 40
    if draw_pos == 0:
        crt.append('\n')
    if draw_pos in [pos - 1, pos, pos + 1]:
        crt.append('#')
    else:
        crt.append('.')
ops = [line.strip() for line in open("input.txt", "r").readlines()]
cycle = 0
pos = 1
crt = []
for op in ops:
    if op == 'noop':
        cycle += 1
        draw(crt, cycle, pos)
    else:
        cycle += 1
        draw(crt, cycle, pos)
        cycle += 1
        draw(crt, cycle, pos)
        pos += int(op.split()[1])
print("".join(crt))