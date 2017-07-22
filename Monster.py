class Monster():
    def __init__(self, name, maxhp, hp, attack, miss, xpgain, goldgain):
        self.name = name
        self.hp = hp
        self.maxhp = maxhp
        self.attack = attack
        self.xpgain = xpgain
        self.goldgain = goldgain
        self.miss = miss

#                name, maxhp, hp, attack, miss, xpgain, goldgain
BanditIG = Monster("Bandit", 50, 50, 5, 10, 15, 10)
DraugrIG = Monster("Draugr", 70, 70, 7, 10, 20, 15)

BanditChiefIG = Monster("Bandit Chief", 100, 100, 20, 5, 1500, 50)
DraugrDeathoIG = Monster("Draugr Death Overlord", 140, 140, 28, 5, 2000, 75)

mobs = [BanditIG, DraugrIG]
bossMobs = [BanditChiefIG, DraugrDeathoIG]
