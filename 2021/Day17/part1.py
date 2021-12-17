from itertools import count
#minX = 60
#maxX = 94
minY = -171
maxY = -136
best_top_height = 0
for velY in count(1, 1):
    y = 0
    print(velY)
    top_height = sum([velY - t for t in range(velY)])
    for t in count(0, 1):
        y += velY
        velY -= 1
        if y <= maxY and y >= minY:
            best_top_height = top_height
            print(best_top_height)
            break
        if y < minY:
            break
