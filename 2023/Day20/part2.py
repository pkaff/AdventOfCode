from collections import defaultdict
import math
from functools import reduce

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

class Module():
    def __init__(self, name, neighbours):
        self.name = name
        self.neighbours = neighbours[:]

class Output(Module):
    def Receive(self, from_name, signal):
        print(f"Output received signal {signal} from {from_name}")

    def Send(self):
        return []

class Broadcaster(Module):
    def Send(self):
        to_send = []
        for neighbour in self.neighbours:
            to_send.append((0, neighbour))
        return to_send

class FlipFlop(Module):
    def __init__(self, name, neighbours):
        super(FlipFlop, self).__init__(name, neighbours)
        self.is_on = False
        self.should_send = False

    def Receive(self, from_name, signal):
        if signal == 0:
            self.should_send = True
            if self.is_on:
                self.is_on = False
            else:
                self.is_on = True
        else:
            self.should_send = False

    def Send(self):
        to_send = []
        if self.should_send:
            for neighbour in self.neighbours:
                if self.is_on:
                    to_send.append((1, neighbour))
                else:
                    to_send.append((0, neighbour))
        return to_send

class Conjunction(Module):
    def __init__(self, name, neighbours):
        super(Conjunction, self).__init__(name, neighbours)
        self.last_signals = {}

    def AddInputs(self, inputs):
        for input in inputs:
            self.last_signals[input] = 0

    def Receive(self, from_name, signal):
        self.last_signals[from_name] = signal

    def Send(self):
        to_send = []
        for neighbour in self.neighbours:
            if all(self.last_signals.values()):
                to_send.append((0, neighbour))
            else:
                to_send.append((1, neighbour))
        return to_send

config = [line.strip().split(' -> ') for line in open("input.txt", "r").readlines()]
modules = {}
conjunctions = [module[1:] for module, _ in config if '&' in module]
conjunction_inputs = defaultdict(lambda: [])
modules['output'] = Output('output', [])
for module, neighbours in config:
    neighbours = neighbours.split(', ')
    if module == 'broadcaster':
        modules[module] = Broadcaster(module, neighbours)
    elif '%' in module:
        modules[module[1:]] = FlipFlop(module[1:], neighbours)
    elif '&' in module:
        modules[module[1:]] = Conjunction(module[1:], neighbours)
    for neighbour in neighbours:
        if neighbour in conjunctions:
            conjunction_inputs[neighbour].append(module[1:])
for conjunction in conjunctions:
    modules[conjunction].AddInputs(conjunction_inputs[conjunction])

n_presses = 0
nodes_of_interest = ['pr', 'fv', 'bt', 'rd']
first_found = {}
while True:
    # Button
    n_presses += 1
    to_process = [[('broadcaster', modules['broadcaster'].Send())]]
    while to_process:
        modules_and_signals = to_process.pop(0)
        next_to_process = []
        for module_name, sent in modules_and_signals:
            for signal, neighbour in sent:
                if neighbour in nodes_of_interest:
                    if signal == 0:
                        if neighbour not in first_found:
                            first_found[neighbour] = n_presses
                        if all(n in first_found for n in nodes_of_interest):
                            print(reduce(lambda a, b: lcm(a, b), first_found.values()))
                            exit()
                if neighbour not in modules:
                        continue
                modules[neighbour].Receive(module_name, signal)
                next_to_process.append((neighbour, modules[neighbour].Send()))
        if next_to_process:
            to_process.append(next_to_process)
