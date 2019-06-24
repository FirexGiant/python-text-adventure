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

def Look(userInput, player):
    if player.inventory.HasItems():
        for item in player.inventory.items:
            if item.name.lower() in userinput:
                typeout("You look through your items...")
                typeout(item.desc)
                return 
    if player.inventory.HasFood():
        for food in player.inventory.food:
            if food.name.lower() in userInput:
                typeout("You look through your food...")
                typeout(food.desc)
                print("Heals for {0}.".format(str(food.healingAmount)))
                return 
    if player.currentLocation.inventory.HasItems():
        for item in player.currentLocation.inventory.items:
            if item.name.lower() in userInput:
                typeout("You look around...")
                typeout(item.desc)
                return 
    if player.currentLocation.inventory.HasFood():
        for food in player.currentLocation.inventory.food:
            if food.name.lower() in userInput:
                typeout("You look around...")
                typeout(food.desc)
                print("Heals for {0}.".format(str(food.healingAmount)))
                return 
    if userInput.strip() == "look":
        if player.currentLocation.lookDesc == None:
            typeout(player.currentLocation.desc)
        else:
            typeout(player.currentLocation.lookDesc)
        return 
    if "around" in userInput:
        if player.currentLocation.lookDesc == None:
            typeout(player.currentLocation.desc)
        else:
            typeout(player.currentLocation.lookDesc)
        return 
    if "here" in userInput:
        if player.currentLocation.lookDesc == None:
            typeout(player.currentLocation.desc)
        else:
            typeout(player.currentLocation.lookDesc)
        return 
    print("I don't see that anywhere.")
    return 

def Take(userInput, player):
    if player.currentLocation.inventory.HasItems():
        for item in player.currentLocation.inventory.items:
            if item.name.lower() in userInput:
                player.inventory.AddItem(item)
                player.currentLocation.inventory.RemoveItem(item)
                print("{0} added to items.".format(item.name))
                return
    if player.currentLocation.inventory.HasFood():
        for food in player.currentLocation.inventory.food:
            if food.name.lower() in userInput:
                player.inventory.AddFood(food)
                player.currentLocation.inventory.RemoveFood(food)
                print("{0} added to food.".format(food.name))
                return
    print("I don't see that anywhere.")
    return

def Eat(userInput, player):
    if player.inventory.HasFood():
        for food in player.inventory.food:
            if food.name.lower() in userInput:
                food.Heal(player)
                player.inventory.RemoveFood(food)
                return
    if player.currentLocation.inventory.HasFood():
        for food in player.currentLocation.inventory.food:
            if food.name.lower() in userInput:
                food.Heal(player)
                player.currentLocation.inventory.RemoveFood(food)
                return
    print("I don't see that anywhere.")
    return

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
        elif "look" in userInput:
            Look(userInput, player)
        elif "take" in userInput:
            Take(userInput, player)
        elif "eat" in userInput:
            Eat(userInput, player)
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