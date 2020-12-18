class OperatorWrapper:
    def __init__(self, i):
        self.i = int(i)
    def __add__(self, other):
        return OperatorWrapper(self.i + other.i)
    def __sub__(self, other): #hack to get add and mul to same precedence
        return OperatorWrapper(self.i * other.i)
    def __str__(self):
        return str(self.i)
    def __repr__(self):
        return str(self)
    def __int__(self):
        return int(self.i)

expressions = ["".join(["OperatorWrapper("+c+")" if c.isdigit() else c for c in l.rstrip().replace('*', '-') if c != ' ']) for l in open("input.txt", "r").readlines()]
print(sum(list(map(lambda x: int(eval(x)), expressions))))


