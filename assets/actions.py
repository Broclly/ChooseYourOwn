# Originally created on 10/10/2024
## Asset for a school project
### DO NOT COPY WITHOUT PERMISSION FROM BROCLLY

from assets.player import Player
from colorama import Fore
from assets.rooms import Room
from assets.rooms import roomsList

player = Player()
room = Room()

class Action:
    def __init__(self, actionSelected=None):
        self.actionSelected = actionSelected if actionSelected else "ERROR!"


    def getOptions(self):
        loopIteration = 0
        for x in player.currentRoom.options:
            print(str(loopIteration + 1) + ". " + player.currentRoom.options[loopIteration])
            loopIteration += 1
    def fallAsleep(self):
        print('You try to get up, but faitgue gets the best of you. \n \n"Maybe I should just fall asleep and wake up another day...." \n \nYou close your eyes, and dream of a better day....')
        player.sleepCounter += 1
    def takeMeds(self):
        print('"Maybe some of my meds will help this headache go away" \n \nYou grab your Xanax and pour out 1. The pills are pretty large after all. With one big gulp of water, you swallow it. \n \n"There we go.. Much better..." \n \nYOU FEEL CALM')
        player.medTox += 1
    def getDressed(self):
        print( '"Eh, may as well get up, getting dressed is always a great day to start the day, no?" \n \nYou go over to your dresser, and grab some clothing; your casual outfit you only wear on Saturday mornings like this. \n \n"Looking good, good looking!" It feels unatural not to hear ' + Fore.RED + 'her ' + Fore.WHITE + 'say it to you anymore...')
        player.wearingClothes = True
    def goOutside(self):
        from main import enterRoom
        print('"I almost forgot! Today is saturday, and I got a whole day to seize. Better go outside." \n\nYou walk out your bedroom door and head downstairs. And then finally, you throw the door open and step outside \n \n"Good morning Silvercity!"')
        player.currentRoom = roomsList["Outside"]
        enterRoom()
    def makeBreakfast(self):
        print("vector!")