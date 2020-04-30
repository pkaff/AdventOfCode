from math import exp
#Gives bottom right number of the ring r
def totalNumbers(r):
	return pow(1+2*r, 2)
	
#Gives bottom right number of the one smaller ring r
def prevTotalNumbers(r):
	return pow(2*r - 1, 2)

input = 368078
ring = [None, 1, 2, 4, 5, 10, 11, 23, 25]
r = 2
done = False
while not done:
	nInRing = totalNumbers(r) - prevTotalNumbers(r)
	newRing = [0]*int(nInRing + 1)
	newRing[0] = None
	for i in range(1, nInRing + 1):
		if i == 1: #First
			newRing[i] = ring[-1] + ring[1]
		elif i == nInRing: #Last
			newRing[i] = newRing[1] + ring[-1] + newRing[i - 1]
		elif i % int(nInRing//4) == 0: #Corner
			newRing[i] = newRing[i - 1] + ring[i - 2*(i//int(nInRing//4))]
		elif (i + 1) % int(nInRing//4) == 0: #Before corner
			if i + 1 == nInRing:
				newRing[i] = newRing[i - 1] + ring[i - 1 - 2*(i//int(nInRing//4))] + ring[i - 2 - 2*(i//int(nInRing//4))] + newRing[1]
			else:
				newRing[i] = newRing[i - 1] + ring[i - 1 - 2*(i//int(nInRing//4))] + ring[i - 2 - 2*(i//int(nInRing//4))]
		elif (i - 1) % int(nInRing//4) == 0: #After corner
			newRing[i] = newRing[i - 1] + newRing[i - 2] + ring[i - 2*(i//int(nInRing//4))] + ring[i - 1 - 2*(i//int(nInRing//4))]
		else: #Side
			tempix = i - 2 - 2*(i//int(nInRing//4))
			if tempix == 0:
				tempix = -1
			newRing[i] = newRing[i - 1] + ring[i - 2*(i//int(nInRing//4))] + ring[i - 1 - 2*(i//int(nInRing//4))] + ring[tempix]
		if newRing[i] > input:
			print (newRing[i])
			done = True
			break
	ring = newRing
	r += 1