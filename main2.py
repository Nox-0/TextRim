import sys
import os
import random
import pickle
import Player
import Monster

#TO DO:
# SHOP, STATS (AND LEVEL STATS), INVENTORY, POTIONS, MAGICKA, RUN, CRIT DAMAGE AND CHANCE, COMPLEX COMBAT, RUN CHANCE AGAINST BOSS
# CONSIDERING MAKING A LEVELXP FUNCTION

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

    if option == "1":
        prefight()
    elif option == "2":
        pass
    elif option == "3":
        pass
    elif option == "4":
        pass
    elif option == "9":
        GameState.saveGame()
    elif option == "0":
        sys.exit()
    else: home()


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
    print("1.) Attack \n2.) Magicka \n3.) Potions \n 5) Run")
    option = input("--> ")
    if option == "1":
        attack()
    elif option == "2":
        magicka()
    elif option == "3":
        potions()
    elif option == "5":
        sys.exit()
    else:
        fight()


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
    gameLoop()

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



#I THOUGHT THIS WOULD BE NICE TO LOOK AT
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

    def missRoll():
        roll = random.randint(1,100)
        return roll




menu()
