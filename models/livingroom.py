from .room import Room
class Livingroom(Room):
    def __init__(self,name):
        self.name = name
        self.capacity = 4
        self.occupants = []
    
    def create_livingroom(self,name):
        return ['LivingRoom called {} has been created successfully!'.format(name), 'green']