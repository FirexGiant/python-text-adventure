class Location:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.items = None 
        self.LocationNorth = None
        self.LocationSouth = None
        self.LocationWest = None
        self.LocationEast = None 

    def HasItems(self):
        if self.items == None:
            return False
        else:
            return True
