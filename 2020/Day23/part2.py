class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    def __eq__(self, other):
        return self.val == other.val
    def __repr__(self):
        if self.next:
            return "val: " + str(self.val) + " next: " + str(self.next.val)
        else:
            return "val: " + str(self.val) + " next: None"

myinput = [7, 1, 6, 8, 9, 2, 5, 4, 3]
prev = None
nodes = {}
for val in myinput:
    nodes[val] = Node(val)
    if prev:
        prev.next = nodes[val]
    prev = nodes[val]
for ix in range(len(myinput), 1000000 + 1):
    nodes[ix + 1] = Node(ix + 1)
    prev.next = nodes[ix + 1]
    prev = nodes[ix + 1]

curNode = nodes[myinput[0]]
maxNode = nodes[1000000]
maxNode.next = curNode
for r in range(10000000):
    pickedup = [curNode.next, curNode.next.next, curNode.next.next.next]
    curNode.next = pickedup[-1].next
    if curNode.val == 1:
        destNode = maxNode
    else:
        destNode = nodes[curNode.val - 1]
    while destNode in pickedup:
        destNode = nodes[destNode.val - 1]
        if destNode.val == 0:
            destNode = maxNode
    pickedup[-1].next = destNode.next
    destNode.next = pickedup[0]
    curNode = curNode.next
print(nodes[1].next.val * nodes[1].next.next.val)