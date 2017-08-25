import Items, os, sys

class Character:
    def __init__(self, name):
        self.name = name
        self.race = ""
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
        self.spellInv = []

        self.smithing = 15
        self.heavyArmour = 15
        self.block = 15
        self.twoHanded = 15
        self.oneHanded = 15
        self.archery = 15
        self.lightArmour = 15
        self.sneak = 15
        self.lockpicking = 15
        self.speech = 15
        self.pickpocket = 15
        self.alchemy = 15
        self.illusion = 15
        self.conjuration = 15
        self.destruction = 15
        self.restoration = 15
        self.alteration = 15
        self.enchanting = 15

    @property
    def attack(self):
        attack = self.baseAttack
        if self.curweap in Items.meleeWeapons:
                weaponAttack = Items.meleeWeapons[self.curweap]["wepAttack"]
                attack += weaponAttack

        return attack
        
