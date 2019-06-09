from os import name
from os import system 

from World import World
world = World()

def clearScreen():
    if name == "nt":
        system("cls")
    else:
        system("clear")

def Look(userInput, player):
    # return True is just to break out of the method so it doesn't print the item desc and the error message
    if userInput == ['look'] or userInput == ['l']:
        print(player.currentLocation.desc)
        return True
    else:
        try:
            userInput.remove('look')
        except:
            userInput.remove('l')
        if player.HasItems():
            for item in player.items:
                itemName = item.name.lower().split()
                if itemName == userInput:
                    print("You look through your items.")
                    print(item.desc)
                    return True
        if player.HasFood():
            for food in player.food:
                foodName = food.name.lower().split()
                if foodName == userInput:
                    print("You look through your food.")
                    print(food.desc)
                    return True
        if player.currentLocation.HasItems():
            for item in player.currentLocation.items:
                itemName = item.name.lower().split()
                if itemName == userInput:
                    print("You look around the area.")
                    print(item.desc)
                    return True
        if player.currentLocation.HasFood():
            for food in player.currentLocation.food:
                foodName = food.name.lower().split()
                if foodName == userInput:
                    print("You look around the area.")
                    print(food.desc)
                    return True
        print("I don't see that anywhere.")

def Take(userInput, player):
    try:
        userInput.remove("take")
    except:
        userInput.remove("pick up")
    if player.currentLocation.HasItems():
        for item in player.currentLocation.items:
            itemName = item.name.lower().split()
            if itemName == userInput:
                player.AddItem(item)
                player.currentLocation.RemoveItem(item)
                return True # This is just here to break out of the method
    if player.currentLocation.HasFood():
        for food in player.currentLocation.food:
            foodName = food.name.lower().split()
            if foodName == userInput:
                player.AddFood(food)
                player.currentLocation.RemoveFood(food)
                return True # This is just here to break out of the method
    print("I don't see that anywhere.")

def Drop(userInput, player):
    userInput.remove('drop')
    if player.HasItems():
        for item in player.items:
            itemName = item.name.lower().split()
            if itemName == userInput:
                player.RemoveItem(item)
                player.currentLocation.AddItem(item)
                return True # This is just here to break out of the method 
    if player.HasFood():
        for food in player.food:
            foodName = food.name.lower().split()
            if foodName == userInput:
                player.RemoveFood(food)
                player.currentLocation.AddFood(food)
                return True # This is just here to break out of the method 
    print("You don't have that.")

def Eat(userInput, player):
    userInput.remove('eat')
    if player.HasFood():
        for food in player.food:
            foodName = food.name.lower().split()
            if foodName == userInput:
                player.Heal(food.healingAmount)
                player.RemoveFood(food)
                return True # This is just here to break out of the method 
    if player.currentLocation.HasFood():
        for food in player.currentLocation.food:
            foodName = food.name.lower().split()
            if foodName == userInput:
                player.Heal(food.healingAmount)
                player.currentLocation.RemoveFood(food)
                return True # This is just here to break out of the method  
    print("I don't see that anywhere.")

def HandleInput(player):
    locationExists = True
    while True: 
        userInput = input(">").lower().split()
        for word in userInput:
            if word == "north" or word == "n":
                if player.HasLocationNorth():
                    player.MoveNorth()
                    return True 
                else:
                    locationExists = False 
            elif word == "south" or word == "s":
                if player.HasLocationSouth():
                    player.MoveSouth()
                    return True
                else:
                    locationExists = False
            elif word == "west" or word == "w":
                if player.HasLocationWest():
                    player.MoveWest()
                    return True
                else:
                    locationExists = False
            elif word == "east" or word == "e":
                if player.HasLocationEast():
                    player.MoveEast()
                    return True
                else:
                    locationExists = False
            elif word == "look" or word == "l":
                Look(userInput, player)
                return True
            elif word == "take" or word == "pick up":
                Take(userInput, player)
                return True
            elif word == "drop":
                Drop(userInput, player)
                return True 
            elif word == "eat":
                Eat(userInput, player)
                return True 
            elif word == "clear" or word == "c":
                clearScreen()
                return True
            elif word == "exit" or word == "quit" or word == "q": # There's no 'e' because 'e' is already being used for moving east
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