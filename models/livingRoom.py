from .room import Room
class LivingRoom(Room):
    def __init__(self,name):
        self.name = name
        self.capacity = 4
        self.occupants = []