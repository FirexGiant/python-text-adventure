from Item import Item 
from Location import Location
from Player import Player

class World:
    def __init__(self):
        self.items = self.CreateItems()
        self.locations = self.CreateLocations()
        self.player = Player(10, 0, 2)
        self.player.loc = self.locations[0]
        self.player.items = self.items 

    def CreateItems(self):
        # Define items 
        banana = Item("Banana", "It's just a normal banana. Very tasty!")

        # Add items to items list 
        items = [banana]
        return items 

    def CreateLocations(self):
        # Define locations 
        loc1 = Location("Location 1", "There is nothing to do here in Location 1.")
        loc2 = Location("Location 2", "There is nothing to do here in Location 2.")
        loc3 = Location("Location 3", "There is nothing to do here in Location 3.")
        loc4 = Location("Location 4", "There is nothing to do here in Location 4.")

        # Add location connections 
        loc1.locNorth = loc2
        loc1.locSouth = loc4
        loc1.locEast = loc3

        loc2.locSouth = loc1

        loc3.locWest = loc1

        loc4.locNorth = loc1

        # Add locations to locations list 
        locs = [loc1, loc2, loc3, loc4]
        return locs 
