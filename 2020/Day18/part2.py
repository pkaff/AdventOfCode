class OperatorWrapper:
    def __init__(self, i):
        self.i = int(i)
    def __sub__(self, other): #hack to get mul lower precedence than add
        return OperatorWrapper(self.i * other.i)
    def __mul__(self, other): #hack to get add lower precedence than mul
        return OperatorWrapper(self.i + other.i)
    def __str__(self):
        return str(self.i)
    def __repr__(self):
        return str(self)
    def __int__(self):
        return int(self.i)

expressions = ["".join(["OperatorWrapper("+c+")" if c.isdigit() else c for c in l.rstrip().replace('*', '-').replace('+', '*') if c != ' ']) for l in open("input.txt", "r").readlines()]
print(sum(list(map(lambda x: int(eval(x)), expressions))))