import re
from collections import defaultdict
from collections import Counter

input = sorted([y.replace('[','').split('] ') for y in [x.replace('\n','') for x in open("input1.txt", "r").readlines()]], key = lambda x: x[0])
idToMinuteSleeping = defaultdict(list)

id = 0
t1 = 0
t2 = 0
for i in input:
	if 'Guard #' in i[1]:
		id = int(re.search(r'\d+', i[1]).group())
	elif 'falls asleep' in i[1]:
		t1 = int(i[0][-2:])		
	elif 'wakes up' in i[1]:
		t2 = int(i[0][-2:])
		for m in range(t1, t2):
			idToMinuteSleeping[id].append(m)

sleepyGuardId = max(idToMinuteSleeping.keys(), key=lambda id: len(idToMinuteSleeping[id]))
print(sleepyGuardId * Counter(idToMinuteSleeping[sleepyGuardId]).most_common(1)[0][0])

sleepyGuardId2 = max(idToMinuteSleeping.keys(), key=lambda id: Counter(idToMinuteSleeping[id]).most_common(1)[0][1])
print(sleepyGuardId2 * Counter(idToMinuteSleeping[sleepyGuardId2]).most_common(1)[0][0])

	