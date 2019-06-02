from Item import Item

class Potion(Item):
    def __init__(self, name, desc, healingAmount):
        Item.__init__(self, name, desc)
        self.healingAmount = healingAmount