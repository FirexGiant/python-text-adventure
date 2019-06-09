class Location:
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc
        self.items = []
        self.food = []
        self.LocationNorth = None
        self.LocationSouth = None
        self.LocationWest = None
        self.LocationEast = None 

    def HasItems(self):
        if self.items == None:
            return False
        else:
            return True

    def AddItem(self, item):
        self.items.append(item)

    def RemoveItem(self, item):
        self.items.remove(item)

    def HasFood(self):
        if self.food == []:
            return False
        else:
            return True
        
    def AddFood(self, food):
        self.food.append(food)

    def RemoveFood(self, food):
        self.food.remove(food)
