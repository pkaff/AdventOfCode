def compare(left, right):
    if type(left) == int and type(right) == int:
        if left < right:
            return -1
        if left > right:
            return 1
        if left == right:
            return 0
    if type(left) == list and type(right) == list:
        minLen = min(len(left), len(right))
        for ix in range(minLen):
            ret = compare(left[ix], right[ix])
            if ret == -1 or ret == 1:
                return ret
        if len(left) < len(right):
            return -1
        if len(left) > len(right):
            return 1
        if len(left) == len(right):
            return 0
    if type(left) == int:
        return compare([left], right)
    if type(right) == int:
        return compare(left, [right])

class MyList:
    def __init__(self, lst, divider=False):
        self.lst = lst
        self.divider = divider
    def __eq__(self, other):
        return self.__cmp__(other) == 0
    def __lt__(self, other):
        return self.__cmp__(other) < 0
    def __gt__(self, other):
        return self.__cmp__(other) > 0
    def __cmp__(self, other):
        return compare(self.lst, other.lst)
    def __str__(self):
        return str(self.lst)
    def __repr__(self):
        return self.__str__()

myin = [MyList(eval(packets.strip('\n'))) for packets in open("input.txt", "r").readlines() if packets != '\n']
myin.append(MyList([[2]], True))
myin.append(MyList([[6]], True))

myin = sorted(myin)
indices = [i + 1 for i, lst in enumerate(myin) if lst.divider]
print(indices[0] * indices[1])
