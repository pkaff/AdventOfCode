myin = list(zip(*[l.replace('\n', '') for l in list(open("input.txt", "r").readlines())]))
gammaRate = ''.join(['1' if col.count('1') > col.count('0') else '0' for col in myin])
epsilonRate = ''.join(['0' if col.count('1') > col.count('0') else '1' for col in myin])
print(int(gammaRate, 2) * int(epsilonRate, 2))
