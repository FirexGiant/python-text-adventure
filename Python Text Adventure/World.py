from Location import Location
from Player import Player
from Item import Item
from Food import Food
from Inventory import Inventory

class World:
    def __init__(self):
        self.CreateInventory()
        self.CreateLocations()
        self.CreatePlayer()

    # Creation methods 
    def CreateInventory(self):
        self.inventory = Inventory()
        self.inventory.items = [
            Item(1, "Paper", "It's a piece of paper that reads, \"Hello adventurer! Have you tried the banana?\""),
            Item(2, "Cup", "It is a cup. You know, like the ones from the movies.")
        ]
        self.inventory.food = [
            Food(1, "Banana", "It's just a normal banana. Very tasty!", 2),
            Food(2, "Apple", "It's just like a banana, except it's not.", 1)
        ]

    def CreateLocations(self):
        self.locations = [
            Location(1, "Circle of Trees", "Light pierces your eyes as you struggle to force them open. \nYou lie on dirt ground in the middle of a circle of trees. You remember nothing. \nBeside you lays a wooden sword. You roll over and grab the sword. \nYou then stab the sword into the ground and slowly lift yourself up. \nYou slip the sword into the belt that is around your waist. \nThere is a dirt path to the north that leads into the darkness of the woods.", "Just go north already.", items = [self.inventory.GetItem(1), self.inventory.GetItem(2)], food = [self.inventory.GetFood(1), self.inventory.GetFood(2)], locationIdNorth = 2),
            Location(2, "Dark Path", "You walk along a dark path. You cannot see much, but you can tell that the path leads north.", locationIdNorth = 3),
            Location(3, "Intersection", "As you walk you come across an intersection. It is sunny now. You see that there are paths leading north, south, west, and east.", locationIdSouth = 2)
        ]

    def CreatePlayer(self):
        self.player = Player(10, 0, 2, self.GetLocation(1))

    # Task methods
    def GetLocation(self, locationId):
        if self.locations == []:
            print("GetLocation() ERROR: There are no locations.")
        else:
            for location in self.locations:
                if location.id == locationId:
                    return location 
            print("GetLocation() ERROR: Location with id '{0}' not found.".format(str(locationId)))

    # Player movement 
    def MovePlayerNorth(self):
        if self.player.HasLocationNorth():
            self.player.currentLocation = self.GetLocation(self.player.currentLocation.locationIdNorth)
            return True 
        else: 
            print("You cannot go north.")
            return False

    def MovePlayerSouth(self):
        if self.player.HasLocationSouth():
            self.player.currentLocation = self.GetLocation(self.player.currentLocation.locationIdSouth)
            return True 
        else:
            print("You cannot go south.")
            return False

    def MovePlayerWest(self):
        if self.player.HasLocationWest():
            self.player.currentLocation = self.GetLocation(self.player.currentLocation.locationIdWest)
            return True
        else:
            print("You cannot go west.")
            return False

    def MovePlayerEast(self):
        if self.player.HasLocationEast():
            self.player.currentLocation = self.GetLocation(self.player.currentLocation.locationIdEast)
            return True
        else:
            print("You cannot go east.")
            return False