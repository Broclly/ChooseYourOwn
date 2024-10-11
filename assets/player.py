# Originally Created on 10/10/2024
## Asset for a school project
### DO NOT COPY WITHOUT CREDITS TO BROCLLY

from assets.rooms import roomsList

class Player:
    def __init__(self): # Initalize the class of player
        self.username = None
        self.itemEquppied = None
        self.currentRoom = roomsList["Bedroom"]
        self.mood = "Distraught"
        self.medTox = 0
        self.sleepCounter = 0
        self.wearingClothes = False