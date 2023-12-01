print(sum([int(list(filter(str.isdigit, line))[0] + list(filter(str.isdigit, line))[-1])  for line in open("input.txt", "r").readlines()]))
