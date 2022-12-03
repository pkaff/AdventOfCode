def toPriority(letter):
    if letter.isupper():
        return ord(letter) - 65 + 27
    if letter.islower():
        return ord(letter) - 96
myin = [set(line) for line in [line.strip() for line in open("input.txt", "r").readlines()]]
print(sum([toPriority(''.join(myin[ix].intersection(myin[ix+1]).intersection(myin[ix+2]))) for ix in range(0, len(myin), 3)]))