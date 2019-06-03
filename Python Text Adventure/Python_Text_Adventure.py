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
    if not player.items == None:
        for item in player.items:
            itemName = item.name.lower().split()
            if itemName == itemToLook:
                print(item.desc)
                return True
    if not player.loc.items == None:
        for item in player.loc.items:
            itemName = item.name.lower().split()
            if itemName == itemToLook:
                print(item.desc)
                return True
    print("I don't see that anywhere.")


def HandleInput(player):
    error = False
    looking = False 
    pos = -1
    while True: 
        userInput = input(">").lower().split()
        for word in userInput:
            pos += 1
            if looking:
                try:
                    userInput.remove('look')
                except:
                    userInput.remove('l')
                Look(userInput, player)
                return True
            if word == "north" or word == "n":
                if player.loc.locNorth == None:
                    error = True
                else:
                    player.loc = player.loc.locNorth
                    return True 
            if word == "south" or word == "s":
                if player.loc.locSouth == None:
                    error = True
                else:
                    player.loc = player.loc.locSouth
                    return True
            if word == "west" or word == "w":
                if player.loc.locWest == None:
                    error = True
                else:
                    player.loc = player.loc.locWest
                    return True
            if word == "east" or word == "e":
                if player.loc.locEast == None:
                    error = True
                else:
                    player.loc = player.loc.locEast
                    return True
            if word == "look" or word == "l":
                looking = True
            if word == "clear" or word == "c":
                clearScreen()
                return True
            if word == "exit" or word == "quit" or word == "q": # There's no 'e' because 'e' is already being used for moving east
                return False
        if error:
            print("You cannot go that way!")
            error = False
        elif looking:
            print(player.loc.desc)
            return True
        else:
            print("I didn't catch that. Please try again.")

def Game(player):
    playing = True
    while playing: 
        print()
        print(player.loc.name)
        print(player.loc.desc)
        playing = HandleInput(player)

print("###########################")
print("#        WELCOME TO       #")
print("#  PYTHON TEXT ADVENTURE  #")
print("###########################")
Game(world.player) 