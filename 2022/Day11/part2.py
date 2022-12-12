from heapq import nlargest
from itertools import accumulate

prime_factors = 1

class Monkey:
    def __init__(self, input_lst):
        global prime_factors
        self.ix = int(input_lst[0].split()[1][-2])
        self.items = [int(item) for item in input_lst[1].split(': ')[1].split(', ')]
        self.op = lambda old: eval(input_lst[2].split(' = ')[1])
        prime_factors *= int(input_lst[3].split(' divisible by ')[-1])
        test_str = "".join(input_lst[3].split(': ')[1]).replace('divisible by', 'x %')
        test_str += ' == 0'
        self.test = lambda x: eval(test_str)
        self.true_branch = int(input_lst[4][-1])
        self.false_branch = int(input_lst[5][-1])
        self.num_inspect = 0
    def receive(self, item):
        self.items.append(item)
    def turn(self, monkeys):
        global prime_factors
        while self.items:
            item = self.items.pop(0)
            self.num_inspect += 1
            new_worry = self.op(item) % (prime_factors)
            if self.test(new_worry):
                monkeys[self.true_branch].receive(new_worry)
            else:
                monkeys[self.false_branch].receive(new_worry)
    def __str__(self):
        printstr = "\nMonkey " + str(self.ix) + " holding items: ["
        for ix, item in enumerate(self.items):
            printstr += str(item)

            if ix != len(self.items) - 1:
                printstr += ', '
        printstr += ']'
        return printstr
    def __repr__(self):
        return str(self)

monkeys = [Monkey(line.split('\n')) for line in open("input.txt", "r").read().split('\n\n')]
print(monkeys)
for round in range(10000):
    for monkey in monkeys:
        monkey.turn(monkeys)
print(list(accumulate(nlargest(2, [monkey.num_inspect for monkey in monkeys]), lambda x, y: x * y))[-1])
