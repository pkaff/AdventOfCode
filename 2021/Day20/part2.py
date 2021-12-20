enh_str, img = open("input.txt", "r").read().replace('.', '0').replace('#', '1').split('\n\n')
img = img.split('\n')
img = {(x, y) for y, l in enumerate(img) for x, c in enumerate(l) if c == '1'}

def calculateNeighbours(x, y):
    return [(xx, yy) for yy in range(y - 1, y + 2) for xx in range(x - 1, x + 2)]

def get_binary_str(img, point, boundary, padding_on):
    neighbours = calculateNeighbours(point[0], point[1])
    binary_str = ''
    for neighbour in neighbours:
        if neighbour in img or (padding_on and neighbour not in boundary):
            binary_str += '1'
        else:
            binary_str += '0'
    return binary_str

def calculateNewActives(actives, cycle):
    maxX = max(actives, key = lambda i : i[0])[0]
    maxY = max(actives, key = lambda i : i[1])[1]
    minX = min(actives, key = lambda i : i[0])[0]
    minY = min(actives, key = lambda i : i[1])[1]
    boundary = {(x, y) for x in range(minX, maxX + 1) for y in range(minY, maxY + 1)}
    newActives = set()
    for y in range(minY - 1, maxY + 2):
        for x in range(minX - 1, maxX + 2):
            point = (x, y)
            padding_on = (cycle % 2) == 1
            binary_str = get_binary_str(actives, point, boundary, padding_on)
            enh_str_ix = int(binary_str, 2)
            if enh_str[enh_str_ix] == '1':
                newActives.add(point)
    return newActives

for cycle in range(50):
    img = calculateNewActives(img, cycle)
print(len(img))
