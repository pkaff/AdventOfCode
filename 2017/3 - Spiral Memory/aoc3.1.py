from math import exp
#Gives bottom right number of the ring r
def totalNumbers(r):
	return pow(1+2*r, 2)
	
#Gives bottom right number of the one smaller ring r
def prevTotalNumbers(r):
	return pow(2*r - 1, 2)

#Returns all 4 corners of the ring of number n
def corners(n):
	r = ring(n)
	return [totalNumbers(r) - 2*r*i for i in range(4)]

#Returns the ring for the number n
def ring(n):
	r = 1
	while totalNumbers(r) < n:
		r += 1
	return r
	
#Returns which side the number is on, 'N', 'W', 'S' 'E' or 'C' for corner
def side(n):
	c = corners(n)
	if n in c:
		return 'C'
	elif n < c[3]:
		return 'E'
	elif n < c[2]:
		return 'N'
	elif n < c[1]:
		return 'W'
	elif n < c[0]:
		return 'S'
	print ("INCONSISTENT SIDE HANDLING")

input = 368078
r = ring(input)

steps = 0
while input > 1:
	s = side(input)
	ptn = prevTotalNumbers(ring(input))
	ptn2 = prevTotalNumbers(ring(ptn))
	baseSub = ptn - ptn2 + 1
	if s == 'C':
		input -= 1 #Can go -1 or +1 step, no matter. -1 is always in the same ring
	elif s == 'E':
		#Special case for first on east side
		if input == ptn + 1:
			input -= 1
		else:
			input -= baseSub
	elif s == 'N':
		input -= baseSub + 2
	elif s == 'W':
		input -= baseSub + 4
	elif s == 'S':
		input -= baseSub + 6
	steps += 1

print (steps)