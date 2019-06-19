from os import name
from os import system 
def clearScreen():
    if name == "nt":
        system("cls")
    else:
        system("clear") 

from Typeout import typeout

from World import World
world = World()

def HandleInput(player): 
    while True:
        done = False 
        # Returns true if player wants to continue playing, false if player wants to quit 
        userInput = input(">").lower()
        if "north" in userInput:
            done = world.MovePlayerNorth()
            if done:
                return True 
        elif "south" in userInput:
            done = world.MovePlayerSouth()
            if done:
                return True
        elif "west" in userInput:
            done = world.MovePlayerWest()
            if done:
                return True
        elif "east" in userInput:
            done = world.MovePlayerEast()
            if done:
                return True
        elif "clear" in userInput:
            clearScreen()
            return True
        elif "exit" in userInput:
            return False 
        elif "quit" in userInput:
            return False 
        else:
            print("I didn't catch that. Try again, maybe?")

def Game(player):
    playing = True 
    while playing:
        player.PrintLocation()
        playing = HandleInput(player)

Game(world.player)