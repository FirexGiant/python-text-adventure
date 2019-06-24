from Typeout import typeout
from Inventory import Inventory

class Player:
    def __init__(self, name, desc, health, minDmg, maxDmg, currentLocation = None, items = [], food = []):
        self.name = name
        self.desc = desc
        self.health = health
        self.maxHealth = maxHealth
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
