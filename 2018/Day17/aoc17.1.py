from collections import defaultdict
import sys

sys.setrecursionlimit(10000)
input = [l.split(', ') for l in open("input.txt", "r").readlines()]
clay = defaultdict(lambda: False)

maxY = 0
minY = 1000000
for i in input:
    if 'x=' in i[0]:
        x = int(i[0][2:])
        for y in range(int(i[1].split('..')[0][2:]), int(i[1].split('..')[1].strip()) + 1):
            clay[(x, y)] = True
            if y > maxY:
                maxY = y
            if y < minY:
                minY = y
    elif 'y=' in i[0]:
        y = int(i[0][2:])
        for x in range(int(i[1].split('..')[0][2:]), int(i[1].split('..')[1].strip()) + 1):
            clay[(x, y)] = True

still = set()
active = set()
def fill(coord, dir=(0, 1)):
    x = coord[0]
    y = coord[1]
    active.add(coord)
    
    below = (x, y + 1)
    
    if not clay[below] and below not in active and 1 <= below[1] <= maxY:
        fill(below)

    if not clay[below] and below not in still:
        return False #blocked in down dir

    left = (x - 1, y)
    right = (x + 1, y)
    lFilled = clay[left] or left not in active and fill(left, dir=(-1, 0))
    rFilled = clay[right] or right not in active and fill(right, dir=(1, 0))
    
    if dir == (0, 1) and lFilled and rFilled:
        still.add((x, y))
        
        while left in active:
            still.add(left)
            left = (left[0] - 1, left[1])
            
        while right in active:
            still.add(right)
            right = (right[0] + 1, right[1])
    
    return dir == (-1, 0) and (lFilled or clay[left]) or dir == (1, 0) and (rFilled or clay[right]) #blocked in left or right dir
    
fill((500, 0))

print(len([pt for pt in still | active if minY <= pt[1] <= maxY]))
print(len([pt for pt in still if minY <= pt[1] <= maxY]))