from Location import Location
from Player import Player
from Item import Item
from Food import Food
from Inventory import Inventory

class World:
    def __init__(self):
        self.CreateInventory()
        self.CreateLocations()

    def CreateInventory(self):
        self.inventory = Inventory()
        inventory.items = [
            Item(1, "Paper", "It's a piece of paper that reads, \"Hello adventurer! Have you tried the banana?\""),
            Item(2, "Cup", "It is a cup. You know, like the ones from the movies.")
        ]
        inventory.food = [
            Food(1, "Banana", "It's just a normal banana. Very tasty!", 2),
            Food(2, "Apple", "It's just like a banana, except it's not.", 1)
        ]

    def CreateLocations(self):
        self.locations = [
            Location(1, "Circle of Trees", "Light pierces your eyes as you struggle to force them open. \nYou lie on dirt ground in the middle of a circle of trees. You remember nothing. \nBeside you lays a wooden sword. You roll over and grab the sword. \nYou then stab the sword into the ground and slowly lift yourself up. \nYou slip the sword into the belt that is around your waist. \nThere is a dirt path to the north that leads into the darkness of the woods.", locationIdNorth = 2),
            Location(2, "Dark Path", "You walk along a dark path. You cannot see much, but you can tell that the path leads north.", locationIdNorth = 3),
            Location(3, "Intersection", "As you walk you come across an intersection. It is sunny now. You see that there are paths leading north, south, west, and east.", locationIdSouth = 2)
        ]