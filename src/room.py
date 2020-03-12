# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items
    def room_in_direction(self, direction):
        directions = {
            "n": self.n_to,
            "s": self.s_to,
            "e": self.e_to,
            "w": self.w_to
        }
        return directions[direction]
    def list_items(self):
        if len(self.items) > 0:
            output = "In the room, you see: "
            for item in self.items:
                if isinstance(item, Item):
                    output += f"{item.name}, "
            return output[:-2]
        else:
            return None
