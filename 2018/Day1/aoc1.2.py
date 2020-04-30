from collections import defaultdict
inputlist = [x.replace('\n','') for x in open("input1.txt", "r").readlines()]
frequencies = defaultdict(int)
freq = 0
done = False
while(not done):
    for i in inputlist:
        freq += eval(i)
        frequencies[freq] += 1
        if (frequencies[freq] == 2):
            print(freq)
            done = True
            break