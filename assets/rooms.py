# Originally Created on 10/08/2024
## Asset for a school project
### DO NOT COPY WITHOUT CREDITS TO BROCLLY

from assets.actions import Action

global actions 
actions = Action()
class Room: # Initalizes the rooms class for name initalization
    def __init__(self, name=None,descript=None,options=None,dialogue=None):
        self.name  = name if name else "ERROR!"
        self.descript = descript if descript else "ERROR!"
        self.options = options if options else "ERROR!"
        self.dialogue = "ERROR!"
        
roomsList = {
    "Bedroom" : Room("Bedroom", "You awake in the small quaint bedroom with a slight headache, seeming to remember doing something last night. There's a half empty bottle of Xanax on your bedside table, the crows nearby are chirping.\n\n",["Go to bed","Take your meds","Get dressed","Leave the house", "Make breakfast"],[actions.fallAsleep,actions.takeMeds,actions.getDressed,actions.goOutside,actions.makeBreak]),
    "Outside" : Room("Outside","The light from the sun gently penetrates the clouds and slightly grazes your face... There's a lady across the street, she notices you...\n\n,"),
    "Jess's House" : Room("Jess's House","The air smells sweetly of cinnamon, pumpkin spice, and apple. A cozy aura floats around in the air around you, surrounding you. All your worries melt away..\n\n."),
    "River of Reflection" : Room("River of Reflection","There's something bittersweet about this place. It reminds you of memories that aren't your own. The winds of change blow as something mischevious is afoot...\n\n"),
    "Church Of Achillies" : Room("Church of Achillies","This place, built to worship the god Achillies, seems ruined. A computer is blinking in the distance, barely on. It has one file on it's desktop...\n\n"),
    "Kitchen" : Room("Kitchen","Your kitchen. Creation of all the food you've eaten recently, and conviently it seems that you have a knife on a cutting board, ready for you\n\n"),
    "Silvercity Bank" : Room("Silvercity Bank","The floors and walls of this marvel institution are prestine and perfectly clean, coated by a shiny gloss. Everything smells of business, suffering and pain. There must be something you can do about this...\n\n") 
}

Decisions = ["Charm the lady", "Murder the lady", "Charm the lady", "Go to the abandoned building"]