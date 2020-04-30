import re
file = open("input.txt", "r")
particles = [[eval(re.sub('[pav=]', '', re.sub('>', ']', re.sub('<', '[', coords.rstrip(','))))) for coords in line.split()] for line in file.readlines()]
print(particles.index(min(particles, key=lambda particle: sum(map(lambda y: abs(y), particle[2])))))