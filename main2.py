import sys, os, random, pickle, Player, Monster, Items

#AN EQUINOX ENTERTAINMENT GAME XD
#SHOULD FOCUS ON:
#TODO: MAKING THE WEAPON AFFECT DAMAGE. <- AFTER THIS IS DONE PUSH TO MASTER
#TO CREATE:
#TODO: LEVELING STATS, POTIONS, MAGICKA/MAGIC, CRIT DAMAGE/CHANCE, SHOP POTIONS, PLAYER CLASSES/ROLES,
#TO IMPROVE:
#TODO: COMBAT, SHOP, BETTER ENEMIES, DYING, EQUIPING

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
    print("\n2) Shop \n3) Inventory \n4) Stats")
    print("\n9) Save Game \n0) Exit")
    option = input("--> ")

    if option == "1": prefight()
    elif option == "2": Shop.shopFront()
    elif option == "3": inventory()
    elif option == "4": stats()
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
    print("1) Attack \n2) Magicka \n3) Potions \n 5) Run")
    option = input("--> ")

    if option == "1": attack()
    elif option == "2": magicka()
    elif option == "3": potions()
    elif option == "5": sys.exit()
    else: fight()


#PLAYER ATTACK FUNCTINO
def playerAttack():
    os.system('cls')
    playerAttack = round(random.uniform(PlayerIG.attack/2, PlayerIG.attack), 0)
    acc = Dice.missRoll() #acc for accuracy
    if acc <= PlayerIG.miss:
        print("You missed!")
        enemyAttack()
    else:
        enemy.hp -= playerAttack
        print("You deal %i damage!"  % playerAttack)

    option = input('')
    if enemy.hp <= 0: win()
    else: enemyAttack()

#ENEMY'S ATTACK FUNCTION
def enemyAttack():
    os.system('cls')
    enemyAttack = round(random.uniform(enemy.attack/2, enemy.attack), 0)
    acc = Dice.missRoll() #acc for accuracy
    if acc <= enemy.miss:
        print("%s missed!" % enemy.name)
        fight()
    else:
        enemy.hp -= playerAttack
        print("%s dealt %i damage!"  % (enemy.name, enemyAttack))

    option = input('')
    if player.hp <= 0: lose()
    else: fight()

#THIS POTION FUNCTION IS WHEN THE PLAYER IS IN BATTLE
def potBattle():
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
    print("You are dead")
    option = input('')
    gameLoop()


#FOR WHEN THE PLAYER IS A PUSSY
def run():
    os.system('cls')
    runum = random.randint(1, 3)
    if runnum == 1:
        print("You have successfully ran away!")
        option = input('')
        gameLoop()
    else:
        print("You failed to get away!")
        option = input('')
        os.system('cls')
        enemyAttack()


#GENERAL INVENTORY OF THE PLAYER
def inventory():
    os.system('cls')
    print("This is your inventory:")
    for items in PlayerIG.inv:
        print(items)

    print("\n1) Potions")
    print("0) Back")
    option = input("--> ")

    if option == "0": gameLoop()
    elif option == "1": potInventory()
    elif option in PlayerIG.inv: Equip.weaponEquip(option)


#THIS POTION INVENTORY IS FOR WHEN THE PLAYER IS NOT IN BATTLE
def potInventory():
    os.system('cls')
    print("%s Health: %d" %(PlayerIG.name, PlayerIG.hp))
    print("0) Back")
    for pot in PlayerIG.potInv:
        print(pot)
    option = input("--> ")

    if option == "0": inventory()
    if option in Character.potInv:
        potInv.remove(option)
        print("You restored %i health!" % option.hpHeal)
        PlayerIG.hp += option.hpHeal
        if PlayerIG.hp > PlayerIG.maxhp:
            PlayerIG.hp = PlayerIG.maxhp
    else: print("You don't have that potion!")


def stats():
    os.system('cls')
    print("Stats:\n")
    print("Name: %s" % PlayerIG.name)
    print("Attack: %i" % PlayerIG.attack)
    print("Gold: %d" % PlayerIG.gold)
    print("Current Weapon: %s" % PlayerIG.curweap)
    print("Health: %i/%i" % (PlayerIG.hp, PlayerIG.maxhp))
    print("Level: ", int(PlayerIG.lvl))
    print("Next: ", int(PlayerIG.lvlNext))
    print("Level percentage: {:.0%}".format(PlayerIG.xp/PlayerIG.lvlNext))
    input("--> ")
    gameLoop()

class Equip:
    def weaponEquip(weapon):
        PlayerIG.curweap = weapon
        print("You have equiped %s." % weapon)
        input("--> ")
        inventory()


class Shop:
    def shopFront():
        os.system('cls')
        print("Welcome to Warmaiden\'s. Now don\'t let the name frighten you, we've got plenty o\' steel for fightin\' men.")
        print("\nGold: %d" % PlayerIG.gold)
        print("1) See Weapons")
        print("2) See Potions")
        print("0) Back")
        option = input("--> ")

        if option == "1": Shop.shopWeapons()
        elif option == "2": Shop.shopPotions()
        elif option == "0": gameLoop()
        else: Shop.shopFront()

    def shopWeapons():
        os.system('cls')
        print("You look like someone who knows how to wield a weapon. Well, you\'ve come to the right place.")
        print("\nGold: %d" % PlayerIG.gold)

        for weapons in Items.buyableWeapons:
            print(weapons.name, ":", weapons.value)

        print("\n0) Back")
        option = input("--> ")

        if option == "0":
            Shop.shopFront()
        elif option in Items.buyWeapons:
            if PlayerIG.gold >= Items.buyWeapons[option]:
                os.system('cls')
                PlayerIG.gold -= Items.buyWeapons[option]
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
        roll = random.randint(1,100)
        return roll




menu()
