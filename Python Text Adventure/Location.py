class Location:
    def __init__(self, id, name, desc, altDescs = [], items = [], food = [], locationIdNorth = None, locationIdSouth = None, locationIdWest = None, locationIdEast = None):
        self.id = id
        self.name = name
        self.desc = desc
        self.altDescs = altDescs
        self.items = items
        self.food = food
        self.locationIdNorth = locationIdNorth
        self.locationIdSouth = locationIdSouth
        self.locationIdWest = locationIdWest
        self.locationIdEast = locationIdEast
