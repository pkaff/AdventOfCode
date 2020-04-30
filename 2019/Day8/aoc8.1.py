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
nZeros = ["".join(layer).count("0") for layer in layers]
bestLayer = "".join(layers[nZeros.index(min(nZeros))])
print(bestLayer.count("1")*bestLayer.count("2"))

