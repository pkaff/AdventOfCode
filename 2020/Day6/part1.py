print(sum([len(set("".join(l.split("\n")))) for l in open("input.txt", "r").read().split("\n\n")]))