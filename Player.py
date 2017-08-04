import Items, os, sys


class Character:
    def __init__(self, name):
        self.name = name
        self.maxhp= 100
        self.hp = self.maxhp
        self.baseAttack = 10
        self.curweap = ""
        self.points = 0
        self.lvl = 1
        self.xp = 0
        self.lvlNext = 10
        self.gold = 1000
        self.miss = 10  #subject to change
        self.inv = []
        self.potInv = []
        self.spellsInv = []

    @property
    def attack(self):
        attack = self.baseAttack
        if self.curweap in Items.meleeWeapons:
                weaponAttack = Items.meleeWeapons[self.curweap]["wepAttack"]
                attack += weaponAttack

        return attack
