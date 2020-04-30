file = open("input.txt", "r")
layers = list(map(lambda x: x.replace(':', ''), file.readlines()))
firewall = [[] for i in range(int(layers[-1].split()[0]) + 1)]
for l in layers:
    firewall[int(l.split()[0])] = int(l.split()[1])
delay = 0
while True:
    caught = False
    for picosecond in range(len(firewall)):
        if (firewall[picosecond] != [] and (picosecond + delay) % (2*(firewall[picosecond] - 1)) == 0):
            caught = True
            break
    if (not caught):
        break
    delay += 1
print(delay)