from Inventory import Inventory

class Location:
    def __init__(self, id, name, desc, pauseOnPeriod = False, altDescs = [], items = [], food = [], locationIdNorth = None, locationIdSouth = None, locationIdWest = None, locationIdEast = None):
        self.id = id
        self.name = name
        self.desc = desc
        self.pauseOnPeriod = pauseOnPeriod # Determines whether or not to pause on periods while running typeout() method for this location's desc
        self.altDescs = altDescs
        self.inventory = Inventory()
        self.inventory.items = items
        self.inventory.food = food
        self.locationIdNorth = locationIdNorth
        self.locationIdSouth = locationIdSouth
        self.locationIdWest = locationIdWest
        self.locationIdEast = locationIdEast
