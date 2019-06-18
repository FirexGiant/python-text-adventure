from Inventory import Inventory

class Location:
    def __init__(self, id, name, desc, pauseOnPeriod = False, altDescs = [], items = [], food = [], locationIdNorth = None, locationIdSouth = None, locationIdWest = None, locationIdEast = None):
        self.id = id
        self.name = name
        self.desc = desc
        self.pauseOnPeriod = pauseOnPeriod
        self.altDescs = altDescs
        self.inventory = Inventory()
        self.inventory.items = items
        self.inventory.food = food
        self.locationIdNorth = locationIdNorth
        self.locationIdSouth = locationIdSouth
        self.locationIdWest = locationIdWest
        self.locationIdEast = locationIdEast
