from Location import Location
from Player import Player
from Item import Item
from Food import Food
from Inventory import Inventory

class World:
    def __init__(self):
        self.items = self.CreateItems()
        self.food = self.CreateFood()
        self.locations = self.CreateLocations()
        self.player = Player(10, 0, 2)
        self.player.currentLocation = self.locations[0]

    def CreateItems(self):
        # Define items 
        paper = Item("Paper", "It's a piece of paper that reads, \"Hello adventurer! Have you tried the banana?\"")

        # Add items to items list 
        items = [paper]
        return items 

    def CreateFood(self):
        # Define foods
        banana = Food("Banana", "It's just a normal banana. Very tasty!", 2)

        # Add foods to foods list 
        foods = [banana]
        return foods

    def CreateLocations(self):
        # Define locations 
        loc1 = Location("Location 1", "There is nothing to do here in Location 1.")
        loc2 = Location("Location 2", "There is nothing to do here in Location 2.")
        loc3 = Location("Location 3", "There is nothing to do here in Location 3.")
        loc4 = Location("Location 4", "There is nothing to do here in Location 4.")

        # Add items to locations 
        loc1.food = [self.food[0]]

        # Add location connections 
        loc1.LocationNorth = loc2
        loc1.LocationSouth = loc4
        loc1.LocationEast = loc3

        loc2.LocationSouth = loc1

        loc3.LocationWest = loc1

        loc4.LocationNorth = loc1

        # Add locations to locations list 
        locs = [loc1, loc2, loc3, loc4]
        return locs 
