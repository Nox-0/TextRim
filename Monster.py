import os
import sys

class Monster():
    def __init__(self, name, maxhp, hp, attack, potgain, xpgain, goldgain):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.attack = attack
        self.potgain = potgain
        self.xpgain = xpgain
        self.goldgain = goldgain

#                name, maxhp, hp, attack, potgain, xpgain, goldgain
GoblinIG = Monster("Goblin", 50, 50, 5, 0, 15, 10)
ZombieIG = Monster("Zombie", 70, 70, 7, 0, 20, 15)

BGoblinIG = Monster("Goblin Boss", 100, 100, 20, 2, 1500, 50)
BZombieIG = Monster("Zombie Boss", 140, 140, 28, 3, 2000, 75)
