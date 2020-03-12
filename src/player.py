# Write a class to hold player information, e.g. what room they are in
# currently.

from item import Item

class Player:
    def __init__(self, name, current_room, inventory = []):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
    def move(self, direction):
        room = self.current_room.room_in_direction(direction)
        if room != None:
            self.current_room = room
            return True
        return False
    def take(self, item_name):
        item = Item.move_item(item_name, self.current_room.items, self.inventory)
        if item is not None:
            item.on_take()
    def drop(self, item_name):
        item = Item.move_item(item_name, self.inventory, self.current_room.items)
        if item is not None:
            item.on_drop()
    def print_inv(self):
        print("\nInventory")
        for item in self.inventory:
            print(f"{item.name}: {item.description}")
        print()
