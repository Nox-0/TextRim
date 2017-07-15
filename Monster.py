class Monster():
    def __init__(self, name, maxhp, hp, attack, miss, potgain, xpgain, goldgain):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.attack = attack
        self.potgain = potgain
        self.xpgain = xpgain
        self.goldgain = goldgain
        self.miss = miss

#                name, maxhp, hp, attack, miss, potgain, xpgain, goldgain
GoblinIG = Monster("Goblin", 50, 50, 5, 10, 0, 15, 10)
DraugrIG = Monster("Draugr", 70, 70, 7, 10, 0, 20, 15)

BGoblinIG = Monster("Goblin Boss", 100, 100, 20, 5, 2, 1500, 50)
BZombieIG = Monster("Zombie Boss", 140, 140, 28, 5, 3, 2000, 75)

mobs = [GoblinIG, DraugrIG]
bossMobs = [BZombieIG, BZombieIG]
