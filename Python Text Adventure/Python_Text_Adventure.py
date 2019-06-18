from os import name
from os import system 
def clearScreen():
    if name == "nt":
        system("cls")
    else:
        system("clear") 

from time import sleep
from keyboard import is_pressed
from keyboard import wait
def typeout(string, delay = 0.035, newline = True, pauseOnPeriod = False):
    for char in string:
        print(char, end='', flush=True)
        if is_pressed('space'):
            # Quickly write out the rest of the string 
            delay = 0
            pauseOnPeriod = False 
        elif char == '.' and pauseOnPeriod:
            wait('enter')
        sleep(delay)
    print()

from World import World
world = World()

def HandleInput(player): 
    while True:
        done = False 
        # Returns true if player wants to continue playing, false if player wants to quit 
        userInput = input(">").lower()
        if "north" in userInput:
            if player.HasLocationNorth():
                player.currentLocation = world.GetLocation(player.currentLocation.locationIdNorth)
                done = True
            else:
                print("You cannot go that way!")
            if done:
                return True 
        elif "south" in userInput:
            if player.HasLocationSouth():
                player.currentLocation = world.GetLocation(player.currentLocation.locationIdSouth)
                done = True
            else:
                print("You cannot go that way!")
            if done:
                return True
        elif "west" in userInput:
            if player.HasLocationWest():
                player.currentLocation = world.GetLocation(player.currentLocation.locationIdWest)
                done = True
            else:
                print("You cannot go that way!")
            if done:
                return True
        elif "east" in userInput:
            if player.HasLocationEast():
                player.currentLocation = world.GetLocation(player.currentLocation.locationIdEast)
                done = True
            else:
                print("You cannot go that way!")
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
        # Print out player's current location info
        print()
        print(player.currentLocation.name)
        typeout(player.currentLocation.desc, pauseOnPeriod = player.currentLocation.pauseOnPeriod)
        # Handle player input
        playing = HandleInput(player)

Game(world.player)