from World import World
world = World()
world.player.loc = world.locations[0]

def HandleInput(player):
    while True:
        error = False
        userInput = input(">").lower().split()
        for word in userInput:
            if word == "north" or word == "n":
                if world.player.loc.locNorth == None:
                    error = True
                else:
                    world.player.loc = world.player.loc.locNorth
                    return True 
            if word == "south" or word == "s":
                if world.player.loc.locSouth == None:
                    error = True
                else:
                    world.player.loc = world.player.loc.locSouth
                    return True
            if word == "west" or word == "w":
                if world.player.loc.locWest == None:
                    error = True
                else:
                    world.player.loc = world.player.loc.locWest
                    return True
            if word == "east" or word == "e":
                if world.player.loc.locEast == None:
                    error = True
                else:
                    world.player.loc = world.player.loc.locEast
                    return True
            if word == "look" or word == "l":
                return True
            if word == "quit" or word == "q":
                return False
        if error:
            print("You cannot go that way!")
            error = False
        else:
            print("I didn't catch that. Please try again.")

playing = True
while playing:
    print()
    print(world.player.loc.name)
    print(world.player.loc.desc)
    playing = HandleInput(world.player)
