#VALUE IS SELL/BUY PRICE

class Melee:
    def __init__(self, name, value, damage):
        self.name = name
        self.value = value
        self.damage = damage

greatSword = Melee("Great Sword", 40, 15)

class Potion:
    def __init__(self, name, value, hpHeal, quantity):
        self.name = name
        self.value = value
        self.hpHeal = hpHeal
        self.quantity = 1

cheapPotion = Potion("Cheap Potion", 10, 50, 1)

#SHOP ITEMS:
buyWeapons = {
    greatSword.name: greatSword.value
}
