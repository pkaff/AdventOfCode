import sys
from collections import defaultdict
input = open("input.txt", "r").read()
width = 25
height = 6
wLayers = []
for w in range(0, len(input), width):
    wLayers.append(input[w : w + width])
layers = []
for h in range(0, len(wLayers), height):
    layers.append(wLayers[h : h + height])

image = ["2"] * (height * width)
for layer in layers:
    ix = 0
    for row in layer:
        for d in row:
            if image[ix] == "2" and d != "2":
                image[ix] = d
            ix += 1
print(image)