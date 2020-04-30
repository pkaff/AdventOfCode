file = open("input.txt", "r")
layers = list(map(lambda x: x.replace(':', ''), file.readlines()))
firewall = [[] for i in range(int(layers[-1].split()[0]) + 1)]
for l in layers:
    firewall[int(l.split()[0])] = [0, int(l.split()[1]), 1]
severity = 0
for picosecond in range(len(firewall)):
    if (firewall[picosecond] != [] and firewall[picosecond][0] == 0):
        severity += picosecond * firewall[picosecond][1]
    for f in firewall:
        if f != []:
            nextPos = f[0] + f[2]
            if nextPos == f[1] or nextPos == -1:
                f[2] *= -1
            f[0] = f[0] + f[2]
print (severity)