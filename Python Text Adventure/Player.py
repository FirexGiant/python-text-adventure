from Typeout import typeout
from Inventory import Inventory

class Player:
    def __init__(self, health, minDmg, maxDmg, currentLocation = None, items = [], food = []):
        self.health = health
        self.minDmg = minDmg
        self.maxDmg = maxDmg
        self.currentLocation = currentLocation
        self.inventory = Inventory()
        self.inventory.items = items
        self.inventory.food = food 

    def PrintLocation(self):
        print()
        print(self.currentLocation.name)
        print()
        typeout(self.currentLocation.desc)

    def PrintItems(self):
        for item in self.inventory.items:
            typeout("{0} ".format(item.name), newline = False)
        print()

    def PrintFood(self):
        for food in self.inventory.food:
            typeout("{0} ".format(food.name), newline = False)
        print()

    def PrintStats(self):
        typeout("Health: {0}".format(str(self.health)))
        typeout("Min damage: {0}".format(str(self.minDmg)))
        typeout("Max damage: {0}".format(str(self.maxDmg)))
        typeout("Items:")
        self.PrintItems()
        typeout("Food:")
        self.PrintFood()

    # Check for locations 
    def HasLocationNorth(self):
        if self.currentLocation.locationIdNorth == None:
            return False
        else:
            return True 

    def HasLocationSouth(self):
        if self.currentLocation.locationIdSouth == None:
            return False
        else:
            return True

    def HasLocationWest(self):
        if self.currentLocation.locationIdWest == None:
            return False
        else:
            return True

    def HasLocationEast(self):
        if self.currentLocation.locationIdEast == None:
            return False
        else:
            return True 
