buffer = [0]
nSteps = 377
curPos = 0
for i in range(1, 2018):
    curPos += nSteps
    curPos = (curPos % len(buffer)) + 1
    buffer.insert(curPos, i)
print(buffer[buffer.index(2017) + 1])