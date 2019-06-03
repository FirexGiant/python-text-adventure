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
