from Item import Item

class Food(Item):
    def __init__(self, id, name, desc, healingAmount):
        Item.__init__(self, id, name, desc)
        self.healingAmount = healingAmount

    def Heal(self, thingToHeal):
        thingToHeal.health += self.healingAmount
        print("Healed by {0}!".format(str(self.healingAmount)))