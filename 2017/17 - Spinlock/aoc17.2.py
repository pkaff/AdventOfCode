atPosOne = 0
nSteps = 377
curPos = 0
for i in range(1, 50000000):
    curPos += nSteps
    curPos = (curPos % i) + 1
    if curPos == 1:
        atPosOne = i
print(atPosOne)