from os import name
from os import system 

from World import World
world = World()

def clearScreen():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def Look(itemToLook, player):
    # return True is just to break out of the function so it doesn't print the item desc and the error message
    if itemToLook == ['look'] or itemToLook == ['l']:
        print(player.currentLocation.desc)
        return True
    else:
        try:
            itemToLook.remove('look')
        except:
            itemToLook.remove('l')
        if player.HasItems():
            for item in player.items:
                itemName = item.name.lower().split()
                if itemName == itemToLook:
                    print(item.desc)
                    return True
        if player.currentLocation.HasItems():
            for item in player.currentLocation.items:
                itemName = item.name.lower().split()
                if itemName == itemToLook:
                    print(item.desc)
                    return True
        print("I don't see that anywhere.")

def HandleInput(player):
    locationExists = True
    while True: 
        userInput = input(">").lower().split()
        for word in userInput:
            if word == "north" or word == "n":
                if player.HasLocationNorth():
                    player.currentLocation = player.currentLocation.LocationNorth
                    return True 
                else:
                    locationExists = False 
            if word == "south" or word == "s":
                if player.HasLocationSouth():
                    player.currentLocation = player.currentLocation.LocationSouth
                    return True
                else:
                    locationExists = False
            if word == "west" or word == "w":
                if player.HasLocationWest():
                    player.currentLocation = player.currentLocation.LocationWest
                    return True
                else:
                    locationExists = False
            if word == "east" or word == "e":
                if player.HasLocationEast():
                    player.currentLocation = player.currentLocation.LocationEast
                    return True
                else:
                    locationExists = False
            if word == "look" or word == "l":
                Look(userInput, player)
                return True
            if word == "clear" or word == "c":
                clearScreen()
                return True
            if word == "exit" or word == "quit" or word == "q": # There's no 'e' because 'e' is already being used for moving east
                return False
        if not locationExists:
            print("You cannot go that way!")
            locationExists = True
        else:
            print("I didn't catch that. Please try again.")

def Game(player):
    playing = True
    while playing: 
        player.PrintLocation()
        playing = HandleInput(player)

print("###########################")
print("#        WELCOME TO       #")
print("#  PYTHON TEXT ADVENTURE  #")
print("###########################")
Game(world.player) 