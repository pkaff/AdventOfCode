from itertools import product
import csv
file = open("input2.txt", "r")
reader = csv.reader(file, dialect='excel-tab')
checksum = 0
for row in reader:
	find = False
	for i in range(len(row) - 1):
		for j in range(i + 1, len(row)):
			ri = int(row[i])
			rj = int(row[j])
			if ri % rj == 0:
				checksum += ri // rj
				find = True
				break
			if rj % ri == 0:
				checksum += rj // ri
				find = True
				break
		if find:
			break
	
print (checksum)