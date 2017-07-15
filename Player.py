import Items

inventory[]

class Character:
    def __init__(self, name):
        self.name = name
        self.maxhp= 100
        self.hp = self.maxhp
        self.base_attack = 10
        self.pots = 2
        self.weap = [""]
        self.curweap = [""]
        self.points = 3
        self.lvl = 1
        self.xp = 0
        self.lvlNext = 10

    @property
    def attack(self):
        attack = self.base_attack

    @property
    def critAttack(self):
        critAttack = 1.2 * attack

    @property
    def missChance(self):
        miss = 5

    #@property
    #def critChance(self):
    #    critChance = 0.1

"""
@property
def attack(self):
    attack = self.base_attack
    if self.curweap == "Rusty Sword":
        attack += 5

    if self.curweap == "Great Sword":
        attack += 15

    if self.curweap == "Stick":
        attack += 2

    if self.curweap == "Blood Sword":
        attack += 50

    return attack
"""
