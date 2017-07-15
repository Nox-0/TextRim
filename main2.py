import sys
import os
import random
import pickle
import Player
import Monster

#TO DO:
#FIGHT, SHOP, STATS (AND LEVEL STATS), INVENTORY, POTIONS, MAGICKA, RUN

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
        bNum = random.choice(Monster.bossMobs)
        enemy = bNum
        fight()
    else:
        enemy = random.choice(Monster.mobs)
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

def playerAttack:
    

#FOR WHEN THE PLAYER IS A PUSSY
def run():
    os.system('cls')
    runum = random.randint(1, 3)
    if runnum == 1:
        print("You have successfully ran away!")
        option = input('')
        start1()
    else:


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
menu()
