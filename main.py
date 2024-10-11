# Originally Created on 10/03/2024
## Created as a school project
### DO NOT COPY WITHOUT CREDITS TO BROCLLY

import time
from colorama import Fore
import os
from assets.values import hashValues
from assets.actions import Player
from assets.actions import Action

endingsCompleted = "!!ERROR!!"
endingsHashFile = "assets/endings.txt"
player = Player()
actions = Action()

def fileLocator():
    directoryLocation = os.path.realpath(__file__)
    os.chdir(directoryLocation[0:-8])

def welcome():
    global nameSelected

    print("Welcome to Joshua's Choose Your Own Adventure Story!")
    nameSelected = input("Please put in your username for this story: ")
    print("Alright then! Welcome,", nameSelected," and have fun on your journey!!")
    player.username = nameSelected
def hashCheck():
    global endingsCompleted
    loopIteration = 0
    validHash = 0


    fd = open(endingsHashFile)
    hashRead = fd.read()

    for x in hashValues:
        if hashValues[loopIteration] == int(hashRead):
            validHash = 1
            endingsCompleted = str(loopIteration)
            break
        else:
            loopIteration = loopIteration + 1
        
    if validHash == 1:
        print("Save state hash is valid, proceeding with game...\n\n")
    else:
        print(Fore.RED + "Invalid save state hash...")
        time.sleep(1)
        print(Fore.YELLOW + "!!WARNING THIS MEANS THAT YOUR HASH HAS BEEN CORRUPTED OR MODIFIED!!" + Fore.WHITE)
        time.sleep(1/2)
        print("Resetting hash back to default...")
        time.sleep(3)
        fd = open(endingsHashFile, "w")
        fd.write(str(hashValues[0]))
        print("Success! This program will terminate, and re-run the check with a valid hash. Please, don't modify your hash.")
        time.sleep(3)
        quit()

def statusReport():
    os.system('cls')
    print("==========")
    print("Mood: " + player.mood)
    print("Endings Completed: " + endingsCompleted)
    print("Username: " + player.username)
    print("Current Room: " + player.currentRoom.name)
    if player.medTox > 0:
        print("Med Toxcicity: " + player.medTox)
    print("==========")


def enterRoom():
    print(player.currentRoom.descript)
    print("You look around, what shall you do?")
    actions.getOptions()
    choice = input("Input corresponding integer: ")
    print(player.currentRoom.options[(choice-1)])
    
    
def setup():
    fileLocator()
    hashCheck()
    welcome()

def main():
    statusReport()
    enterRoom()


setup()
main()