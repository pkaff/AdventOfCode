from itertools import count
minX = 60
maxX = 94
minY = -171
maxY = -136
minVelY = minY - 1
minVelX = 1
maxVelX = maxX + 1
maxVelY = 170 + 1 # from part 1
n_hits = 0
for startVelX in range(minVelX, maxVelX):
    for startVelY in range(minVelY, maxVelY):
        x = 0
        y = 0
        velX = startVelX
        velY = startVelY
        for t in count(0, 1):
            x += velX
            y += velY
            if velX > 0:
                velX -= 1
            velY -= 1
            if y <= maxY and y >= minY and x <= maxX and x >= minX:
                n_hits += 1
                break
            if y < minY or x > maxX:
                break
print(n_hits)
