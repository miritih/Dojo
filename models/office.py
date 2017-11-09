from .room import Room
class Office(Room):
    def __init__(self,office_name):
        self.name = office_name
        self.capacity = 6
        self.occupants = []
        
    def create_office(self,name):
        return ['An office called {} has been created successfully!'.format(name), 'green']