def toPriority(letter):
    if letter.isupper():
        return ord(letter) - 65 + 27
    if letter.islower():
        return ord(letter) - 96
myin = [''.join(set(line[:len(line)//2]).intersection(set(line[len(line)//2:]))) for line in [line.strip() for line in open("input.txt", "r").readlines()]]
print(sum(list(map(toPriority, myin))))