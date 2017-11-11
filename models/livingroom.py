from .room import Room
class Livingroom(Room):
    def __init__(self,name):
        self.name = name
        self.capacity = 4
        self.occupants = []