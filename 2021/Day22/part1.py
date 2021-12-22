reboot_steps = [line.split() for line in open("input.txt", "r").read().split('\n') if line]
for ix, kv in enumerate(reboot_steps):
    coords = [list(map(int, coord.replace('x=', '').replace('y=', '').replace('z=', '').split('..'))) for coord in kv[1].split(',')]
    reboot_steps[ix] = (kv[0], coords)

oncubes = set()
for mode, (xlims, ylims, zlims) in reboot_steps[:20]:
    cuboid = {(x, y, z) for x in range(xlims[0], xlims[1] + 1) for y in range(ylims[0], ylims[1] + 1) for z in range(zlims[0], zlims[1] + 1)}
    if mode == 'on':
        oncubes |= cuboid
    else:
        oncubes -= cuboid
print(len(oncubes))
