import sys
import os
import random
import pickle
import Player
import Monster
import Items

melee = {"Great Sword":40, "Stick":5, "Blood Sword":200, "Rusty Sword":10}

def main():
    os.system('cls')
    print("Welcome to TextRim™!\nJk this shit aint trademarked lol we too poor haha XD :*\n")
    print("1.) Start")
    print("2.) Load")
    print("0.) Exit")
    option = input("--> ")
    if option == "1":
        start()
    elif option == "2":
        if os.path.exists("savefile") == True:
            os.system('cls')
            with open('savefile', 'rb') as f:
                global PlayerIG
                PlayerIG = pickle.load(f)
            print("Loaded Save State...")
            option = input('')
            menu1()
        else:
            print("You have no save file for this game.")
            option = input('')
            main()
    elif option == "0":
        sys.exit()
    else:
        main()

def start():
    os.system('cls')
    print("Hello, what is your name?")
    option = input("--> ")
    global PlayerIG
    PlayerIG = Player.Player(option)
    start0()

def start0():
    os.system('cls')
    print("Welcome, %s!" % PlayerIG.name)
    option = input('')
    start1()

def start1():
    os.system('cls')
    print("Stats:\n")
    print("Name: %s" % PlayerIG.name)
    print("Attack: %i" % PlayerIG.attack)
    print("Gold: %d" % PlayerIG.gold)
    print("Current Weapon: %s" % PlayerIG.curweap)
    print("Potions: %d" % PlayerIG.pots)
    print("Health: %i/%i" % (PlayerIG.hp, PlayerIG.maxhp))
    print("Level: ", int(PlayerIG.lvl))
    print("Next: ", int(PlayerIG.lvlNext))
    print("Level percentage: {:.0%}".format(PlayerIG.xp/PlayerIG.lvlNext))
    input('')
    menu1()

def menu1():
    os.system('cls')
    print("1.) Fight\n2.) Store\n3.) Save\n4.) Stats\n5.) Inventory\n6.) Level Points\n0.) Back")
    option = input("--> ")
    if option == "1":
        prefight()
    elif option == "2":
        store()
    elif option == "3":
        os.system('cls')
        with open('savefile', 'wb') as f:
            pickle.dump(PlayerIG, f)
            print("\nGame has been saved!\n")
        option = input('')
        menu1()
    elif option == "4":
        start1()
    elif option == "5":
        inventory()
    elif option == "6":
        level()
    elif option == "0":
        main()
    else: menu1()

def inventory():
    os.system('cls')
    print("What do you want to do?\n1.) Equip Weapon\n\n0.) Back")
    option = input("--> ")
    if option == "1":
        equip()
    elif option == "0":
        menu1()

def equip():
    os.system('cls')
    print("What do you want to equip?")
    for weapon in PlayerIG.weap:
        print(weapon)
    print("\n0.) Back")
    option = input('--> ')
    if option == PlayerIG.curweap:
        os.system('cls')
        print("You already have that weapon equipped!")
        option = input('')
        equip()
    elif option == "0":
        os.system('cls')
        inventory()
    elif option in PlayerIG.weap:
        os.system('cls')
        PlayerIG.curweap = option
        print("You have equipped %s!" % option)
        option = input('')
        equip()
    else:
        os.system('cls')
        print("You don't have %s in your inventory!" % option)
        option = input('')
        equip()


def prefight():
    global enemy
    enemynum = random.randint(1, 2)
    if enemynum == 1:
        bnum = random.randint (1, 10)
        if bnum == 1:
            enemy = Monster.BGoblinIG
            print("---- WARNING ----\nYOU ARE ABOUT TO FIGHT A BOSS!")
        else:
            enemy = Monster.GoblinIG
    elif enemynum == 2:
        bnum = random.randint (1, 10)
        if bnum == 1:
            enemy = Monster.BZombieIG
            print("---- WARNING ----\nYOU ARE ABOUT TO FIGHT A BOSS!")
        else:
            enemy = Monster.ZombieIG
    else:
        prefight()
    enemy.hp = enemy.maxhp
    fight()

def fight():
    os.system('cls')
    print("%s              vs            %s" % (PlayerIG.name, enemy.name))
    print("%s\'s Health: %d/%d          %s\'s Health: %d/%d" % (PlayerIG.name, PlayerIG.hp, PlayerIG.maxhp, enemy.name, enemy.hp, enemy.maxhp))
    print("Potions: %i" % PlayerIG.pots)
    print("1.) Attack\n2.) Drink Potion\n3.) Run")
    option = input("--> ")
    if option == "1":
        attack()
    elif option == "2":
        drinkpot()
    elif option == "3":
        run()
    else:
        fight()

def attack():
    os.system('cls')
    PAttack = round(random.uniform(PlayerIG.attack/2, PlayerIG.attack), 0)
    EAttack = round(random.uniform(enemy.attack/2, enemy.attack), 0)
    if PAttack == round(PlayerIG.attack/2, 0):
        print("You miss!")
    else:
        enemy.hp -= PAttack
        print("You deal %i damage!"  % PAttack)
    option = input('')
    if enemy.hp <= 0:
        win()
    os.system('cls')
    if EAttack == round(enemy.attack/2, 0):
        print("The %s missed!" % enemy.name)
    else:
        PlayerIG.hp -= EAttack
        print("The %s deals %i damage!" % (enemy.name, EAttack))
    option = input('')
    if PlayerIG.hp <= 0:
        dead()
    else:
        fight()

def drinkpot():
    os.system('cls')
    if PlayerIG.pots == 0:
        print("You don't have any potions!")
        option = input('')
    else:
        PlayerIG.pots -= 1
        PlayerIG.hp += 50
        if PlayerIG.hp > PlayerIG.maxhp:
            PlayerIG.hp = PlayerIG.maxhp
        print("You drank a potion! 50 hp has been restored!")
        option = input('')
    os.system('cls')
    EAttack = round(random.uniform(enemy.attack/2, enemy.attack), 0)
    if EAttack == enemy.attack/2:
        print("The %s missed!" % enemy.name)
    else:
        PlayerIG.hp -= EAttack
        print("The %s deals %i damage!" % (enemy.name, EAttack))
    option = input('')
    if PlayerIG.hp <= 0:
        dead()
    else:
        fight()

def run():
    os.system('cls')
    runnum = random.randint(1, 3)
    if runnum == 1:
        print("You have successfully ran away!")
        option = input('')
        start1()
    else:
        print("You failed to get away!")
        option = input('')
        os.system('cls')
        EAttack = round(random.uniform(enemy.attack/2, enemy.attack), 0)
        if EAttack == round(enemy.attack/2, 0):
            print("The %s missed!" % enemy.name)
        else:
            PlayerIG.hp -= EAttack
            print("The %s deals %i damage!" % (enemy.name, EAttack))
        option = input('')
        if PlayerIG.hp <= 0:
            dead()
        else:
            fight()

def win():
    os.system('cls')
    PlayerIG.gold += enemy.goldgain
    PlayerIG.pots += enemy.potgain
    PlayerIG.xp += enemy.xpgain
    while PlayerIG.xp >= PlayerIG.lvlNext:
        PlayerIG.lvl += 1
        PlayerIG.xp = PlayerIG.xp - PlayerIG.lvlNext
        PlayerIG.lvlNext = round(PlayerIG.lvlNext * 1.5)
        PlayerIG.points += 1
    print("You have defeated the %s!" % enemy.name)
    print("You found %i gold!" % enemy.goldgain)
    print("You have recieved %i potions!\n" % enemy.potgain)
    print("Experience gained: %i" % enemy.xpgain)
    print("Current level: %i" % PlayerIG.lvl)
    print("Level percentage: {:.0%}".format(PlayerIG.xp/PlayerIG.lvlNext))
    option = input('')
    menu1()

def dead():
    os.system('cls')
    print("You are dead")
    option = input('')
    main()

def store():
    os.system('cls')
    print("Welcome to the shop!\n\nWhat would you like to buy?")
    print("Melee: ", melee)
    print("\nPotion - 40 Gold")
    print("\nYou have %i Gold" % PlayerIG.gold)
    print("\n0.) Back\n")
    option = input('--> ')

    if option in melee:
        if PlayerIG.gold >= melee[option]:
            os.system('cls')
            PlayerIG.gold -= melee[option]
            PlayerIG.weap.append(option)
            print("You have bought a %s" % option)
            option = input('')
            store()

        else:
            os.system('cls')
            print("You don't have enough gold!")
            option = input('')
            store()

    elif option == "Potion":
        if PlayerIG.gold >= 40:
            os.system('cls')
            PlayerIG.gold -= 40
            PlayerIG.pots += 1
            print("You have bought a %s" % option)
            option = input('')
            store()

        else:
            os.system('cls')
            print("You don't have enough gold!")
            option = input('')
            store()

    elif option == "0":
        menu1()

    else:
        os.system('cls')
        print("That item does not exist")
        option = input('')
        store()

def level():
    os.system('cls')
    print("Points available: ", PlayerIG.points)
    print("What would you like to level up:\n1.) Strength (Attack increase)\n2.) Dexterity (Gold gain increase)\n3.) Intelligence (Store prices decrease)\n\n0.) Back")
    option = input('--> ')
    if option == "0":
        os.system('cls')
        menu1()
    elif PlayerIG.points <= 0:
        os.system('cls')
        print("You don't have enough points!")
        option = input('')
        level()
    elif option == "1":
        os.system('cls')
        PlayerIG.attack += 1
        PlayerIG.points -= 1
        print("You have increased Strength!")
        option = input('')
        level()
    elif option == "2":
        os.system('cls')
        GoblinIG.goldgain += 2
        ZombieIG.goldgain += 2
        BGoblinIG.goldgain += 5
        BZombieIG.goldgain += 5
        PlayerIG.points -= 1
        print("You have increased Dexterity!")
        option = input('')
        level()
    elif option == "3":
        os.system('cls')
        for key, value in list(melee.items()): melee[key] = round(value * .9)
        PlayerIG.points -= 1
        print("You have increased Intelligence!")
        option = input('')
        level()
    else:
        level()


main()
