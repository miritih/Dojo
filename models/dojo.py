from models.fellow import Fellow
from models.staff import Staff
from models.livingRoom import LivingRoom
from models.office import Office

class Dojo(object):
    def __init__(self):
        self.offices = []
        self.livingrooms = []
        self.fellows = []
        self.staff = []
        self.rooms = []
        self.all_employees = []
        self.wants_accomodation = []

    def create_room(self, name, room_type):
        if room_type not in ['office', 'livingspace']:
            return 'Only offices and livingspaces allowed!'
        if not isinstance(name, str):
            return 'Room names can only be strings!'
        else:
            if room_type == 'office':
                # create an office
                pass
            elif room_type.lower() == 'livingspace'.lower():
                # create a livingspace
                pass
                
    def add_person(self, name, person_type, wants_accomodation='N'):
        if not isinstance(name, str) or not isinstance(person_type, str):
            return 'names and person type should be a strings!'
        if person_type.lower() not in ['fellow', 'staff']:
            return 'Person type can only be a  fellow or a staff!'
        else:
            if person_type.lower() == 'fellow':
                # create a fellow
                name = name.capitalize()
                fellow = Fellow(name)
                self.fellows.append(name)

    
    

   