import os
from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

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

# items and rooms w/items

knife = Item("knife", "knife made from the claw of a tiger")
potion = Item("potion", "The potion retores +10 hit points")
book_of_spells = Item("book_of_spells", "little black book_of_spells")

room['overlook'].items = [potion]
room['treasure'].items = [knife]
room['narrow'].items = [book_of_spells]

# Main

player_name = input("Welcome to the game of passages. What is your name?: ")
new_player = Player(player_name, room['outside'])

print(f"Current location: { new_player.players_room.name }\n")

print(new_player.players_room.description)

def get_an_item():
    item_choice = input("What do you want to do? (enter 'take' or 'leave'): ")

    for i in new_player.players_room.items:
        if item_choice == "take":
            new_player.items.append(i)
            new_player.players_room.items.remove(i)
        elif item_choice =="leave":
            print(f"You left the {i} behind.\n")
        elif item_choice == 'q':
            print("Come back and play again.")
            os._exit(0)
        else:
            print("Option not available.\n")
            get_an_item()

def new_location():
    print(new_player.players_room)
    if len(new_player.players_room.items) > 0:
        get_an_item()
        print(f"\n{new_player} \n")

def wrong_direction():
    print("You can not go in that direction - try again...\n")
    
user_choice = ''
while user_choice != 'q':
    user_choice = input("Please pick a direction (n, s, e, w): ").lower()
    if user_choice == 'n':
        try:
            new_player.players_room.n_to
            new_player.players_room = new_player.players_room.n_to
            new_location()
        except:
            wrong_direction()
    elif user_choice == 's':
        try:
            new_player.players_room.s_to
            new_player.players_room = new_player.players_room.s_to
            new_location()
        except:
            wrong_direction()
    elif user_choice == 'e':
        try:
            new_player.players_room
            new_player.players_room = new_player.players_room.e_to
            new_location()
        except:
            wrong_direction()
    elif user_choice == 'w':
        try:
            new_player.players_room
            new_player.players_room = new_player.players_room.w_to
            new_location()
        except:
            wrong_direction()
    elif user_choice == 'q':
        print("Come back and play again.")
    else:
        print("Pick again, something went wrong...\n")