from models.fellow import Fellow
from models.staff import Staff
from models.livingRoom import LivingRoom
from models.office import Office

class Dojo(object):
    def __init__(self):
        self.offices = {}
        self.livingrooms = {}
        self.fellows = [] 
        self.staff = []
        self.rooms = {}
        self.all_employees = []
        self.accomodated_fellows = []

    def create_room(self, name, room_type):
        if not isinstance(name, str):
                return ['Room names can only be strings!','red']
        if room_type not in ['office', 'livingroom']:
            return ['Only offices and livingrooms allowed!','red']
        if name in self.rooms:
            return ['Room {} already exists!'.format(name),'red']
        else:
            if room_type.lower() == 'office':
                self.room = Office(name)
                self.offices[name] = self.room.occupants 
                self.rooms[name] = [room_type, self.room.occupants]
                return ['An office called {} has been created successfully!'.format(name),'green']
            elif room_type.lower() == 'livingroom':
                self.room = LivingRoom(name)
                self.livingrooms[name] = self.room.occupants
                self.rooms[name] = [room_type, self.room.occupants]
                return ['A LivingRoom called {} has been created successfully!'.format(name),'green']
              
    def add_person(self, name, person_type, wants_accomodation='N'):
        """implementation of add_person command. create a staff or a fellow and assign them a room"""
        if not isinstance(name, str) or not isinstance(person_type, str):
            return 'names and person type should be a strings!'
        if person_type.lower() not in ['fellow', 'staff']:
            return 'Person type can only be a fellow or a staff!'
        else:
            if person_type.lower() == 'fellow':
                fellow = Fellow(name) #create an instance of Fellow
                self.fellows.append(name)
                self.all_employees.append(name)
                if self.offices:
                    offices_list = list(self.offices.keys()) #create alist of offices
                    checked_offices = [] #store list of offices checked to test if full andassign employee
                    while True:
                        office = random.choice(list(self.offices))
                        if len(self.offices[office]) < 6:
                            self.offices[office].append(name)
                            print('Fellow {} has been assigned office {}!'.format(name,office))
                            break
                        if office not in checked_offices:
                            checked_offices.append(office)
                        if checked_offices == offices_list:
                            print('All offices are full, create a new office before recruiting new members!')
                            break
                else:
                    print('No office to assign!')
                if wants_accomodation.lower() in ['y','yes','yeah']:
                    self.accomodated_fellows.append(name)
                if wants_accomodation.lower() in ['y','yes','yeah'] and self.livingrooms:
                    livingrooms_list = list(self.livingspaces.keys())
                    checked_livingrooms = []
                    while True:
                        room = random.choice(list(self.livingrooms))
                        if len(self.livingrooms[room]) < 4:
                            self.livingrooms[room].append(name)
                            print('Fellow %s has been assigned livingroom %s!' % (name, room))
                            break
                        if room not in checked_livingspaces:
                            checked_livingrooms.append(room)
                        if checked_livingrooms == livingrooms_list:
                            print('All livingrooms are full at the moment!')
                            break
                return ('Fellow %s has been added successfully!' % (name))
            elif person_type.lower() == 'staff':
                if wants_accomodation.lower() in ['y','yes','yeah']:
                    print('Staff can not be allocated livingrooms!')
                staff = Staff(name)
                self.staff.append(name)
                self.all_employees.append(name)
                if self.offices:
                    offices_list = list(self.offices.keys()) #create alist of offices
                    checked_offices = [] #store list of offices checked to test if full andassign employee
                    while True:
                        office = random.choice(list(self.offices))
                        if len(self.offices[office]) < 6:
                            self.offices[office].append(name)
                            print('Staff {} has been assigned office {}!'.format(name,office))
                            break
                        if office not in checked_offices:
                            checked_offices.append(office)
                        if checked_offices == offices_list:
                            print('All offices are full, create a new office before recruiting!')
                            break
                else:
                    print('No office to assign!')
                return ('Staff %s has been added successfully!' % (name))


    
    

   