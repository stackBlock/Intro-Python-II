# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, players_room):
        self.name = name
        self.players_room = players_room
        self.items = []
        
    def __str__(self):
        stuff = f"{self.name}\n Inventory: "

        for i in self.items:
            stuff += f"{i} "
        return stuff