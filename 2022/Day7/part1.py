class Node:
    def __init__(self, type, parent, size, name):
        self.children = []
        self.type = type
        self.parent = parent
        self.size = size
        self.name = name
    def AddChild(self, type, size, name):
        child = Node(type, self, size, name)
        self.children.append(child)
        return child
    def GetChild(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None
    def CalcSize(self):
        if self.size == 0:
            return sum([child.CalcSize() for child in self.children])
        else:
            return self.size
    def PrintTree(self, prefix=""):
        print(prefix + str(self))
        for c in self.children:
            c.PrintTree(prefix + "  ")
    def SumDirs(self, maxsize):
        tot = 0
        if self.CalcSize() <= maxsize:
            tot = self.CalcSize()
        tot += sum([child.SumDirs(maxsize) for child in self.children if child.type == "dir"])
        return tot
    def __str__(self):
        return self.name + " (" + self.type + ", size=" + str(self.CalcSize()) + ")"

myin = [command.split('\n') for command in ['$' + line.strip('\n') for line in open("input.txt", "r").read().split('$') if line]]
root = Node("dir", None, 0, '/')
cur_node = root

for command in myin[1:]:
    if command[0] == "$ ls":
        for output in command[1:]:
            if "dir" in output:
                cur_node.AddChild("dir", 0, output.split()[1])
            else:
                sz, filename = output.split()
                cur_node.AddChild("file", int(sz), filename)
    elif "$ cd" in command[0]:
        if ".." in command[0]:
            cur_node = cur_node.parent
        else:
            cur_node = cur_node.GetChild(command[0].split()[-1])
#root.PrintTree()
print(root.SumDirs(100000))