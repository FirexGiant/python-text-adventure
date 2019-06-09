class Player:
    def __init__(self, health, minDmg, maxDmg):
        self.health = health
        self.minDmg = minDmg
        self.maxDmg = maxDmg
        self.currentLocation = None
        self.items = []
        self.food = []

    def PrintLocation(self):
        print()
        print(self.currentLocation.name)
        print(self.currentLocation.desc)

    def Heal(self, amountToHeal):
        self.health += amountToHeal
        print("Your health went up by "+ str(amountToHeal) + "!")

    def HasItems(self):
        if self.items == []:
            return False
        else:
            return True 

    def AddItem(self, item):
        self.items.append(item)
        print(item.name + " added to your items!")

    def RemoveItem(self, item):
        self.items.remove(item)
        print("You dropped the " + item.name + ".")

    def HasFood(self):
        if self.food == []:
            return False
        else:
            return True
        
    def AddFood(self, food):
        self.food.append(food)
        print(food.name + " added to your food!")

    def RemoveFood(self, food):
        self.food.remove(food)
        print("You dropped the " + food.name + ".")

    # Check for locations
    def HasLocationNorth(self):
        if self.currentLocation.LocationNorth == None:
            return False
        else:
            return True 

    def HasLocationSouth(self):
        if self.currentLocation.LocationSouth == None:
            return False
        else:
            return True 

    def HasLocationWest(self): 
        if self.currentLocation.LocationWest == None:
            return False
        else:
            return True 

    def HasLocationEast(self):
        if self.currentLocation.LocationEast == None:
            return False
        else:
            return True 

    # Move to locations
    def MoveNorth(self):
        self.currentLocation = self.currentLocation.LocationNorth

    def MoveSouth(self):
        self.currentLocation = self.currentLocation.LocationSouth

    def MoveWest(self):
        self.currentLocation = self.currentLocation.LocationWest

    def MoveEast(self):
        self.currentLocation = self.currentLocation.LocationEast
