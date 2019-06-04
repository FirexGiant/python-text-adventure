class Player:
    def __init__(self, health, minDmg, maxDmg):
        self.health = health
        self.minDmg = minDmg
        self.maxDmg = maxDmg
        self.currentLocation = None
        self.items = None

    def PrintLocation(self):
        print()
        print(self.currentLocation.name)
        print(self.currentLocation.desc)

    def HasItems(self):
        if self.items == None:
            return False
        else:
            return True 

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
