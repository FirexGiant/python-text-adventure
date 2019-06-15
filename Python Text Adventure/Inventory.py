class Inventory:
    def __init__(self):
        self.items = []
        self.food = []

    def HasItems(self):
        if self.items == []:
            return False
        else:
            return True

    def HasFood(self):
        if self.food == []:
            return False
        else:
            return True 

    def AddItem(self, item):
        self.items.append(item)

    def AddFood(self, food):
        self.food.append(food)

    def RemoveItem(self, item):
        self.items.remove(item)

    def RemoveFood(self, food):
        self.food.remove(food)

    def GetItem(self, itemId):
        if self.HasItems():
            for item in self.items:
                if item.id == itemId:
                    return item
            print("Item with id '{0}' not found.".format(itemId))
        else:
            print("Inventory has no items.")

    def GetFood(self, foodId):
        if self.HasFood():
            for food in self.food:
                if food.id == foodId:
                    return food
            print("Food with id '{0}' not found.".format(foodId))
        else:
            print("Inventory has no food.")
