from Item import Item

class Food(Item):
    def __init__(self, id, name, desc, healingAmount):
        Item.__init__(self, id, name, desc)
        self.healingAmount = healingAmount