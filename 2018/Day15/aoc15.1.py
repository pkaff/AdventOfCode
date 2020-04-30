from collections import defaultdict
from collections import deque

class Unit:
    def __init__(self, type, x, y, dmg):
        self.type = type
        self.x = x
        self.y = y
        self.alive = True
        self.hp = 200
        self.dmg = dmg

    def pos(self):
        return self.x, self.y
    
    def attack(self, dmg):
        self.hp -= dmg
        if self.hp <= 0:
            self.alive = False
    def __repr__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")" + " hp: " + str(self.hp) + " dmg: " + str(self.dmg) + " alive" if self.alive else " dead"
    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")" + " hp: " + str(self.hp) + " dmg: " + str(self.dmg) + " alive" if self.alive else " dead"
        
def adjacent(x, y):
    return [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

def order(pos):
    return pos[1], pos[0]

def shortestPath(graph, blockedNodes, start, potentialTargets):
    if start not in graph:
        return [], None
    
    visited = set()
    queue = deque([(start, 0)])
    retDist = None
    closest = []
    
    while queue:
        pos, dist = queue.popleft()
        if retDist is not None and dist > retDist:
            return closest, retDist
        if pos in visited or pos in blockedNodes:
            continue
        visited.add(pos)
        if pos in potentialTargets:
            retDist = dist
            closest.append(pos)
        for n in graph[pos]:
            if n not in visited:
                queue.append((n, dist + 1))
    
    return closest, retDist

input = [[c for c in x.replace('\n', '')] for x in open("input.txt", "r").readlines()]
units = []
graph = defaultdict(list)
for y in range(len(input)):
    for x in range(len(input[y])):
        c = input[y][x]
        if c in "GE":
            units.append(Unit(c, x, y, 3))
            input[y][x] = '.'
for y in range(len(input)):
    for x in range(len(input[y])):
        if input[y][x] == '.':
            for (xx, yy) in adjacent(x, y):
                if 0 <= xx < len(input[y]) and 0 <= yy < len(input) and input[yy][xx] == '.':
                    graph[(x, y)].append((xx, yy))
                    graph[(xx, yy)].append((x, y))

nRounds = 0
notDone = True
while notDone:
    orderedUnits = sorted(units, key = lambda u: order(u.pos()))
    for ix, u in enumerate(orderedUnits):
        if not u.alive:
            continue
        enemies = [e for e in orderedUnits if e.type != u.type and e.alive]
        ePos = [e.pos() for e in enemies]
        
        adjPos = adjacent(*u.pos())

        atkList = [t for t in adjPos if t in ePos]
        if not atkList:
            targetPos = []
            for e in enemies:
                targetPos.extend([p for p in adjacent(*e.pos()) if p in graph])
            
            ouPos = [ou.pos() for ou in orderedUnits if ou.alive and u != ou]

            targets, dist = shortestPath(graph, ouPos, u.pos(), targetPos)
            
            if targets:
                target = min(targets, key = order)
                
                for a in sorted(adjPos, key = order):
                    _, d = shortestPath(graph, ouPos, a, [target])
                    if d == dist - 1:
                        u.x, u.y = a
                        break
            
            atkList = [t for t in adjacent(*u.pos()) if t in ePos]
        
        if atkList:
            enemies = [e for e in enemies if e.pos() in atkList]
            
            targetedEnemy = min(enemies, key = lambda e: (e.hp, order(e.pos())))
            targetedEnemy.attack(3)

            if (len(set(u.type for u in units if u.alive)) == 1):
                if ix == len(orderedUnits) - 1:
                    nRounds += 1
                print(nRounds * sum(u.hp for u in units if u.alive))
                notDone = False
                
    nRounds += 1
