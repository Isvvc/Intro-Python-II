# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
    def move(self, direction):
        room = self.current_room.room_in_direction(direction)
        if room != None:
            self.current_room = room
            return True
        return False
