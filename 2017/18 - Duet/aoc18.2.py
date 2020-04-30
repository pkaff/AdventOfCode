from collections import defaultdict
import threading
from queue import Queue

def IsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

class MessageThread(threading.Thread):
    def __init__(self, qr, qs, id, instructions):
        super(MessageThread, self).__init__()
        self.registers = defaultdict(lambda: 0)
        self.registers['p'] = id 
        self.receiveQ = qr
        self.sendQ = qs
        self.instructions = instructions
        self.id = id
    def run(self):
        #fName = 'output' + str(self.id)
        #fs = open(fName + 's.txt', 'w')
        #fr = open(fName + 'r.txt', 'w')
        #fc = open(fName + 'c.txt', 'w')
        instructions = self.instructions
        registers = self.registers
        sendQ = self.sendQ
        receiveQ = self.receiveQ
        i = 0
        while i < len(instructions):
            parts = instructions[i].split()
            #fc.write(' '.join('{%s: %s}' % r for r in registers.items()))
            #fc.write('\n')
            #for p in parts:
                #fc.write(p + ' ')
            #fc.write('\n')
            #fc.flush()
            if parts[0] == 'snd':
                #fs.write(str(registers[parts[1]]) + '\n')
                #fs.flush()
                sendQ.put(registers[parts[1]])
                if self.id == 1:
                    global sent1
                    sent1 += 1
                    print(sent1) #HACK SINCE NOT SURE HOW TO BREAK DEADLOCK
            elif parts[0] == 'rcv':
                registers[parts[1]] = receiveQ.get(True)
                #fr.write(str(registers[parts[1]]) + '\n')
                #fr.flush()
            else:
                val = 0
                if parts[2] in registers:
                    val = registers[parts[2]]
                else:
                    val = int(parts[2])
                if parts[0] == 'set':
                    registers[parts[1]] = val
                if parts[0] == 'add':
                    registers[parts[1]] += val
                if parts[0] == 'mul':
                    registers[parts[1]] *= val
                if parts[0] == 'mod':
                    if val != 0:
                        registers[parts[1]] %= val
                if parts[0] == 'jgz':
                    jgzVal = 0
                    if IsInt(parts[1]):
                        jgzVal = int(parts[1])
                    else:
                        jgzVal = registers[parts[1]]
                    if jgzVal > 0:
                        i += val - 1
            i += 1

file = open("input.txt", "r")
instructions = file.readlines()

waiting = [False, False]
sent1 = 0

q1 = Queue()
q2 = Queue()

t0 = MessageThread(q1, q2, 0, instructions)
t0.start()

t1 = MessageThread(q2, q1, 1, instructions)
t1.start()

t0.join()
t1.join()
print(sent1)