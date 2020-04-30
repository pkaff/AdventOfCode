import csv
file = open("input2.txt", "r")
reader = csv.reader(file, dialect='excel-tab')
checksum = 0
for row in reader:
	checksum += int(max(row, key=lambda s: int(s))) - int(min(row, key=lambda s: int(s)))
	
print (checksum)