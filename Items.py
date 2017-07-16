#VALUE IS SELL/BUY PRICE

class Melee:
    def __init__(self, name, value, damage, quantity):
        self.name = name
        self.value = value
        self.damage = damage
        self.quantity = 1



#BUYABLE WEAPONS
greatSword = Melee("Great Sword", 40, 15, 1)
woodenSword = Melee("Wooden Sword", 10, 5, 1)

#SHOP LISTINGS
buyableWeapons = [
    greatSword,
    woodenSword
]

#THE OTHER PART OF THE SHOP LISTINGS
buyWeapons = {
    greatSword.name: greatSword.value,
    woodenSword.name: woodenSword.value
}


class Potion:
    def __init__(self, name, value, hpHeal, quantity):
        self.name = name
        self.value = value
        self.hpHeal = hpHeal
        self.quantity = 1

cheapPotion = Potion("Cheap Potion", 10, 50, 1)
