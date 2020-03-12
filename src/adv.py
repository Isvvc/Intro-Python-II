from room import Room
from player import Player
from item import Item

# Declare all the rooms

jug = Item("jug", "a clay pitcher")
pick = Item("pickaxe", "a stone pickaxe")
rock = Item("rock", "just a rock")

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [jug]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [pick, rock]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

name = input("Enter your character's name: ")
player = Player(name, room['outside'])

print("You stand outside a cave enterance.")
print(player.current_room.description)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    cmd = input("-> ")
    
    inputs = cmd.split()

    if len(inputs) == 1:
        if cmd == "q":
            print("You give up on your quest, allowing the Dark Wizard to take over the world.")
            break
        elif cmd in ["n", "s", "e", "w"]:
            if player.move(cmd):
                room = player.current_room
                print(room.name)
                print(room.description)
                if room.list_items() is not None:
                    print(room.list_items())
            else:
                print("You can't go that way.")
        elif cmd == "inv":
            print([x.name for x in player.inventory])
        elif cmd == "help":
            print("Move: n, s, e, w")
            print("Take items: take [item_name], get [item_name]")
            print("View inventory: inv")
            print("Quit: q")
    elif len(inputs) == 2:
        if inputs[0] in ["get", "take"]:
            player.take(inputs[1])
