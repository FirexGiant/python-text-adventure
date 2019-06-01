from World import World
world = World()

def HandleInput(player):
    while True:
        error = False
        userInput = input(">").lower().split()
        for word in userInput:
            if word == "north" or word == "n":
                if player.loc.locNorth == None:
                    error = True
                else:
                    player.loc = player.loc.locNorth
                    return True 
            if word == "south" or word == "s":
                if player.loc.locSouth == None:
                    error = True
                else:
                    player.loc = player.loc.locSouth
                    return True
            if word == "west" or word == "w":
                if player.loc.locWest == None:
                    error = True
                else:
                    player.loc = player.loc.locWest
                    return True
            if word == "east" or word == "e":
                if player.loc.locEast == None:
                    error = True
                else:
                    player.loc = player.loc.locEast
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

def Game(player):
    playing = True
    while playing: 
        print()
        print(player.loc.name)
        print(player.loc.desc)
        playing = HandleInput(player)

Game(world.player)
