import sys, os, random, pickle, Player, Monster, Items, magicka

#A GAME MADE BY THE ONE TRUE GOD.
#TO CREATE:
#TODO: MAGICKA/MAGIC, CRIT DAMAGE/CHANCE, PLAYER RACES, EQUIPMENT REPLACING, LEVELXP FUNCTION, MP CAP, EQUIPMENT, CLASS PERKS, PERK
#TO IMPROVE:
#TODO: COMBAT, SHOP, BETTER ENEMIES, DYING, EQUIPPING

#MAIN MENU
def menu():
    os.system('cls')
    print("----------------------------------------------------------------------")
    print("Welcome to Textrim™, we are extremely rich and totally trademarked it.")
    print("----------------------------------------------------------------------")
    print("\n1) Start New Game \n2) Load game \n0) Exit Game")
    option = input("--> ")

    if option == "1": newGame()
    elif option == "2":
        if os.path.exists("savefile") == True:
            GameState.loadGame()
        else:
            print("You have no save file for this game.")
            option = input()
            menu()
    elif option == "0": sys.exit()
    else: menu()


#STARTING NEW GAME
def newGame():
    os.system('cls')
    print("Hello, what is your name?")
    option = input("--> ")
    global PlayerIG
    PlayerIG = Player.Character(option)
    start()


#CONFIRMING THAT IT THE NAME WORKS
def start():
    os.system('cls')
    print("Welcome, %s!" % PlayerIG.name)
    option = input('')
    gameLoop()


#HOME MENU SCREEN
def gameLoop():
    os.system('cls')
    print("1) Fight")
    print("\n2) Shop \n3) Character \n4) Stats")
    print("\n9) Save Game \n0) Exit")
    option = input("--> ")

    if option == "1": prefight()
    elif option == "2": Shop.shopFront()
    elif option == "3": playerMenu()
    elif option == "9": GameState.saveGame()
    elif option == "0": sys.exit()
    else: gameLoop()


#PREFIGHT WHERE WE DETERMINE WHAT MOB THE PLAYER WILL FACE
def prefight():
    global enemy
    enemyNum = random.randint(1,10)
    if enemyNum == 1:
        enemy = random.choice(Monster.bossMobs)
    else:
        enemy = random.choice(Monster.mobs)

    enemy.hp = enemy.maxhp
    fight()


#THEY FIGHT TO THE DEATH
def fight():
    os.system('cls')
    print("%5s              vs            %5s" % (PlayerIG.name, enemy.name))
    print("Health: %d/%d                   Health: %d/%d" % (PlayerIG.hp, PlayerIG.maxhp, enemy.hp, enemy.maxhp))
    print("1) Attack \n2) Spells \n3) Potions \n5) Run")
    option = input("--> ")

    if option == "1": playerAttack()
    elif option == "2": spellBattle()
    elif option == "3": potBattle()
    elif option == "5": run()
    else: fight()


#PLAYER ATTACK FUNCTINO
def playerAttack():
    os.system('cls')
    playerAttack = round(random.uniform(PlayerIG.attack/2, PlayerIG.attack), 0)
    acc = Dice.missRoll(90) #acc for accuracy
    if acc <= PlayerIG.miss:
        print("You missed!")
        input('')
        enemyAttack()
    else:
        enemy.hp -= playerAttack
        print("You deal %i damage!"  % playerAttack)
        input('')

    if enemy.hp <= 0: win()
    else: enemyAttack()

#ENEMY'S ATTACK FUNCTION
def enemyAttack():
    os.system('cls')
    enemyAttack = round(random.uniform(enemy.attack/2, enemy.attack), 0)
    acc = Dice.missRoll(90)
    if acc <= enemy.miss:
        print("%s missed!" % enemy.name)
        input('')
        fight()
    else:
        PlayerIG.hp -= enemyAttack
        print("%s dealt %i damage!"  % (enemy.name, enemyAttack))
        input('')

    if PlayerIG.hp <= 0: lose()
    else: fight()

#THIS POTION FUNCTION IS WHEN THE PLAYER IS IN BATTLE
def potBattle():
    os.system('cls')
    print("%s's Health: %d/%d" %(PlayerIG.name, PlayerIG.hp, PlayerIG.maxhp))

    for pot in PlayerIG.potInv:
        print(pot)

    print("\n0) Back to fight")
    option = input("--> ")

    if option == "0": fight()
    if option in PlayerIG.potInv:
        PlayerIG.potInv.remove(option)
        healDone = Items.potions[option]["heal"]
        print("You restored %i health!" % healDone)
        PlayerIG.hp += healDone
        if PlayerIG.hp > PlayerIG.maxhp:
            PlayerIG.hp = PlayerIG.maxhp
        input('')
        enemyAttack()
    else: print("You don't have that potion!")
    potInventory()

def spellBattle():
    fight()

#WIN FUNCITONS
def win():
    os.system('cls')
    PlayerIG.gold += enemy.goldgain
    PlayerIG.xp += enemy.xpgain
    while PlayerIG.xp >= PlayerIG.lvlNext:
        PlayerIG.lvl += 1
        PlayerIG.xp = PlayerIG.xp - PlayerIG.lvlNext
        PlayerIG.lvlNext = round(PlayerIG.lvlNext * 1.5)
        PlayerIG.points += 1
    print("You have defeated the %s!" % enemy.name)
    print("You found %i gold!" % enemy.goldgain)
    print("Experience gained: %i" % enemy.xpgain)
    print("Current level: %i" % PlayerIG.lvl)
    print("Level percentage: {:.0%}".format(PlayerIG.xp/PlayerIG.lvlNext))
    option = input('')
    gameLoop()

#LOSE FUNCTION
def lose():
    os.system('cls')
    print("You were bested in combat by %s, however you manage to escape with a sliver health." % enemy.name)
    PlayerIG.hp = 1
    option = input('')
    gameLoop()


#FOR WHEN THE PLAYER IS A PUSSY
def run():
    os.system('cls')
    runnum = random.randint(1, 3)
    if runnum == 1:
        print("You have successfully ran away!")
        option = input('')
        gameLoop()
    else:
        print("You failed to get away!")
        option = input('')
        os.system('cls')
        enemyAttack()


#------------------------------------------------------------------------------
#PLAYER MENU
def playerMenu():
    os.system('cls')
    print("1) Stats \n2) Inventory \n3) Spells \n4) Perks \n\n0) Back")
    option = input('--> ')

    if option == "1": stats()
    elif option == "2": inventory()
    elif option == "3": spellInventory()
    elif option == "4": perks()
    elif option == "0": gameLoop()
    else: playerMenu()

#GENERAL INVENTORY OF THE PLAYER
def inventory():
    os.system('cls')
    for items in PlayerIG.inv:
        print(items)

    print("\n1) See Potions")
    print("0) Back")
    option = input("--> ")

    if option == "0": gameLoop()
    elif option == "1": potInventory()
    elif option in PlayerIG.inv: Equip.weaponEquip(option)
    else: inventory()

def spellInventory():
    os.system('cls')
    for spells in PlayerIG.spellsInv:
        print(spells)

    option = input("--> ")
    if option == "0": gameLoop()
    else: spellInventory()

#THIS POTION INVENTORY IS FOR WHEN THE PLAYER IS NOT IN BATTLE
def potInventory():
    os.system('cls')
    print("%s's Health: %d/%d" %(PlayerIG.name, PlayerIG.hp, PlayerIG.maxhp))

    for pot in PlayerIG.potInv:
        print(pot)

    print("\n0) Back")
    option = input("--> ")

    if option == "0": inventory()
    if option in PlayerIG.potInv:
        PlayerIG.potInv.remove(option)
        healDone = Items.potions[option]["heal"]
        print("You restored %i health!" % healDone)
        PlayerIG.hp += healDone
        if PlayerIG.hp > PlayerIG.maxhp:
            PlayerIG.hp = PlayerIG.maxhp
        input('')
    else: print("You don't have that potion!")
    potInventory()

#------------------------------------------------------------------------------

def stats():
    os.system('cls')
    print("Stats:\n")
    print("Name: %s" % PlayerIG.name)
    print("Attack: %i" % PlayerIG.attack)
    print("Gold: %d" % PlayerIG.gold)
    print("Current Weapon: %s" % PlayerIG.curweap)
    print("Health: %i/%i" % (PlayerIG.hp, PlayerIG.maxhp))
    print("Level: %i" % int(PlayerIG.lvl))
    print("Next: %i" % int(PlayerIG.lvlNext))
    print("Level percentage: {:.0%}".format(PlayerIG.xp/PlayerIG.lvlNext))

    print("\n1) Level Stats (%i points available)" % PlayerIG.points)
    print("0) Back")
    option = input("--> ")

    if option == "1": levelStats()
    elif option == "0": gameLoop()
    else: stats()


def levelStats():
    os.system('cls')
    print("Points Available: %i" % PlayerIG.points)
    print("\n1) Health (Increases health)")
    print("2) Stamina (Increases damage dealt)")
    print("3) Magicka (Increases magic damage dealt)") #and mana capacity soon
    print("\n0) Back")
    option = input("--> ")

    if option == "0": stats()
    if PlayerIG.points <= 0:
        print("You do not have enough points!")
        input("--> ")
        levelStats()
    else:
        if option == "1": healthStat()
        elif option == "2": staminaStat()
        elif option == "3": magickaStat()
        else: levelStats()

def healthStat():
    os.system('cls')
    PlayerIG.points -= 1
    PlayerIG.maxhp += 10
    PlayerIG.hp += 10
    print("Your health has increased by 10 points!")
    input('')
    levelStats()


def staminaStat():
    os.system('cls')
    PlayerIG.points -= 1
    PlayerIG.baseAttack += 5
    print("Your base attack has increased by 5 points!")
    input('')
    levelStats()

def magickaStat():
    os.system('cls')
    PlayerIG.points -= 1
    PlayerIG.maxhp += 10
    PlayerIG.hp += 10
    print("Your health has increased by 10 points!")
    input('')
    levelStats()


#------------------------------------------------------------------------------

class Equip:
    def weaponEquip(weapon):
        PlayerIG.curweap = weapon
        PlayerIG.inv.remove(weapon)
        print("You have equipped your %s." % weapon)
        input("--> ")
        inventory()


class Shop:
    def shopFront():
        os.system('cls')
        print("Welcome to Warmaiden\'s. Now don\'t let the name frighten you, we've got plenty o\' steel for fightin\' men.")
        print("\nGold: %d" % PlayerIG.gold)
        print("1) See Weapons")
        print("2) See Potions")
        print("3) See Spells")
        print("\n0) Back")
        option = input("--> ")

        if option == "1": Shop.shopWeapons()
        elif option == "2": Shop.shopPotions()
        elif option == "3": Shop.shopSpells()
        elif option == "0": gameLoop()
        else: Shop.shopFront()

    def shopWeapons():
        os.system('cls')
        print("You look like someone who knows how to wield a weapon. Well, you\'ve come to the right place.")
        print("\nGold: %d" % PlayerIG.gold)

        for weapons in Items.meleeWeapons:
            print(weapons, ":", Items.meleeWeapons[weapons]["value"], "gold")

        print("\n0) Back")
        option = input("--> ")

        if option == "0": Shop.shopFront()
        elif option in Items.meleeWeapons:
            if PlayerIG.gold >= Items.meleeWeapons[option]["value"]:
                os.system('cls')
                PlayerIG.gold -= Items.meleeWeapons[option]["value"]
                PlayerIG.inv.append(option)
                print("You have bought a %s" % option)
                option = input('')
                Shop.shopWeapons()
            else:
                os.system('cls')
                print("You don't have enough gold!")
                option = input('')
                store()
        else: Shop.shopWeapons()

    def shopPotions():
        os.system('cls')
        print("You'll find tonics, salves, poultices and potions on my shelves. Browse to your heart's content.")
        print("\nGold: %d \n" % PlayerIG.gold)

        for potions in Items.potions:
            print(potions, ":", Items.potions[potions]["value"], "gold")

        print("\n0) Back")
        option = input("--> ")

        if option == "0": Shop.shopFront()
        elif option in Items.potions:
            if PlayerIG.gold >= Items.potions[option]["value"]:
                os.system('cls')
                PlayerIG.gold -= Items.potions[option]["value"]
                PlayerIG.potInv.append(option)
                print("You have bought a %s" % option)
                option = input('')
                Shop.shopPotions()
            else:
                os.system('cls')
                print("You don't have enough gold!")
                option = input('')
                store()
        else: Shop.shopPotions()

    def shopSpells():
        os.system('cls')
        print("Gold: %d \n" % PlayerIG.gold)
        for spells in magicka.attackSpells:
            print(spells, ":", magicka.attackSpells[spells]["value"], "gold")

        print("\n0) Back")
        option = input("--> ")

        if option == "0": Shop.shopFront()
        elif option in magicka.attackSpells:
            if PlayerIG.gold >= magicka.attackSpells[option]["value"]:
                os.system('cls')
                PlayerIG.gold -= magicka.attackSpells[option]["value"]
                PlayerIG.spellInv.append(option)
                print("You have bought a %s spell" % option)
                option = input('')
                Shop.shopSpells()
            else:
                os.system('cls')
                print("You don't have enough gold!")
                option = input('')
                store()
        else: Shop.shopSpells()


#GAME STATE
class GameState:
    def loadGame():
        os.system('cls')
        with open('savefile', 'rb') as f:
            global PlayerIG
            PlayerIG = pickle.load(f)
        print("Loaded Save State...")
        option = input('')
        gameLoop()

    def saveGame():
        os.system('cls')
        with open('savefile', 'wb') as f:
            pickle.dump(PlayerIG, f)
            print("\nGame has been saved!\n")
        option = input()
        gameLoop()

#DICE ROLL CLASS - HANDLES COMBAT RNG
class Dice:
    def critRoll(num): #DOESNT DO ANYTHING YET
        roll = random.randint(num, 1)
        return roll

    def missRoll(num):
        roll = random.randint(1, num)
        return roll




menu()
