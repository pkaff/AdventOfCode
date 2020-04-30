import re
from copy import deepcopy

class Group:
    def __init__(self, team, units, hp, weaknesses, immunities, dmg, dmgType, initiative):
        self.team = team
        self.units = int(units)
        self.hp = int(hp)
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.dmg = int(dmg)
        self.dmgType = dmgType
        self.initiative = int(initiative)
    def testAttack(self, g):
        if g.dmgType in self.weaknesses:
            return g.power() * 2
        if g.dmgType in self.immunities:
            return 0
        return g.power()
    def attack(self, g):
        dmg = g.power()
        if g.dmgType in self.weaknesses:
            dmg *= 2
        if g.dmgType in self.immunities:
            dmg = 0
        prevUnits = self.units
        self.units -= dmg // self.hp
        return prevUnits - self.units
    def power(self):
        return self.units * self.dmg
    def __repr__(self):
        return "<" + str(self.team) + "; nUnits: " + str(self.units) + "; unitHp: " + str(self.hp) + ", Weaknesses: [" + ' '.join(self.weaknesses) + "], Immunities: [" + ' '.join(self.immunities) + "], unitDmg: " + str(self.dmg) + ", DmgType: " + str(self.dmgType) + ", initiative: " + str(self.initiative) + ">"
    def __str__(self):
        return "<" + str(self.team) + "; nUnits: " + str(self.units) + "; unitHp: " + str(self.hp) + ", Weaknesses: [" + ' '.join(self.weaknesses) + "], Immunities: [" + ' '.join(self.immunities) + "], unitDmg: " + str(self.dmg) + ", DmgType: " + str(self.dmgType) + ", initiative: " + str(self.initiative) + ">"

input = [l.replace('\n','') for l in open("input.txt", "r").readlines() if l != '\n']
team = ''
groups = []
regex = re.compile(r"(\d+) units each with (\d+) hit points (\([^)]*\) )?with an attack that does (\d+) (\w+) damage at initiative (\d+)")
for i in input:
    if i == 'Immune System:' or i == 'Infection:':
        team = i.rstrip(':')
    else:
        rgxRes = regex.match(i)
        units, hp, elements, dmg, dmgType, initiative = rgxRes.groups()
        immunities = []
        weaknesses = []
        if elements:
            elements = elements.rstrip(' )').lstrip('(')
            for s in elements.split('; '):
                if s.startswith('weak to '):
                    weaknesses = s[len('weak to '):].split(', ')
                elif s.startswith('immune to '):
                    immunities = s[len('immune to '):].split(', ')
        g = Group(team, units, hp, weaknesses, immunities, dmg, dmgType, initiative)
        groups.append(g)
initAliveGroups = sorted([g for g in groups if g.units > 0], key = lambda u: (u.power(), u.initiative), reverse=True)
boost = 1
while True:
    aliveGroups = deepcopy(initAliveGroups)
    for g in aliveGroups:
        if g.team == 'Immune System':
            g.dmg += boost
    aliveGroups = sorted([g for g in aliveGroups], key = lambda u: (u.power(), u.initiative), reverse=True)
    while len(set(g.team for g in aliveGroups)) == 2:
        #target selection
        combat = []
        targeted = set()
        for a in aliveGroups:
            enemies = sorted([e for e in aliveGroups if e.team != a.team], key = lambda e: (e.testAttack(a), e.power(), e.initiative), reverse=True)
            target = next((e for e in enemies if e.testAttack(a) != 0 and e not in targeted), None)
            if not target:
                continue
            combat.append((a, target))
            targeted.add(target)
        #combat
        combat = sorted(combat, key = lambda c: c[0].initiative, reverse=True)
        anyKilled = False
        nKilled = 0
        for a, d in combat:
            if a.units <= 0:
                continue
            killed = d.attack(a)
            nKilled += killed
            if killed != 0:
                anyKilled = True
        aliveGroups = sorted([g for g in aliveGroups if g.units > 0], key = lambda u: (u.power(), u.initiative), reverse=True)
        if not anyKilled:
            break
    if len(set(g.team for g in aliveGroups)) == 1 and aliveGroups[0].team == 'Immune System':
        print(sum([u.units for u in aliveGroups]))
        break
    boost += 1
