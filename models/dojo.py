from models.fellow import Fellow
from models.staff import Staff
from models.livingroom import Livingroom
from models.office import Office
from termcolor import colored
import sys
import random


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
        if room_type.lower() not in ['office', 'livingroom']:
            return ['Only offices and livingrooms allowed!','red']
        if name in self.rooms:
            return ['Room {} already exists!'.format(name),'red']
        else:
            class_=getattr(sys.modules[__name__], room_type.capitalize())
            room = class_(name)
            self.rooms[name]=[] #dict of all rooms.
            if room_type.lower()=='office':
                self.offices[name] = []
            else:
                self.livingrooms[name] = room.occupants
            return ['{} {} has been created successfully!'.format(room_type.capitalize(),name),'green']    
              
    def add_person(self, name, person_type, wants_accomodation='N'):
        """implementation of add_person command. create a staff or a fellow and assign them a room"""
        if not isinstance(name, str) or not isinstance(person_type, str):
            return 'names and person type should be a strings!'
        if person_type.lower() not in ['fellow', 'staff']:
            return 'Person type can only be a fellow or a staff!'
        else:
            if person_type.lower() == 'fellow':
               # fellow = Fellow(name) #create an instance of Fellow
                self.fellows.append(name) #append to list of all fellows
                self.all_employees.append(name) # append to list of all 
                if self.offices:
                    self.assign_random_office(name,6)
                else:
                    print(colored('No office to assign!',"red"))
                if wants_accomodation.lower() in ['y','yes','yeah'] and self.livingrooms:
                    self.accomodated_fellows.append(name)
                    livingrooms_list = list(self.livingrooms.keys()) #list of all livingrooms
                    checked_livingrooms = [] #add room here afer each check. to avoid checking same room twice
                    while True:
                        room = random.choice(list(self.livingrooms))
                        if len(self.livingrooms[room]) < 4:
                            self.livingrooms[room].append(name)
                            print(colored('%s has been assigned livingroom %s!' % (name, room),'green'))
                            break
                        if room not in checked_livingrooms:
                            checked_livingrooms.append(room)
                        if checked_livingrooms == livingrooms_list:
                            print(colored('All livingrooms are full at the moment!',"red"))
                            break
                else:
                     print(colored('No Livingroom to assign OR You choose not to be accomodated !',"cyan"))
                return (colored('Fellow %s has been added successfully!' % (name),"green"))
                
            elif person_type.lower() == 'staff':
                if wants_accomodation.lower() in ['y','yes','yeah']:
                    print(colored('Staff can not be allocated livingrooms!',"red"))
                #staff = Staff(name)
                self.staff.append(name)
                self.all_employees.append(name)
                if self.offices:
                    self.assign_random_office(name,6) #call assign_random_office
                else:
                    print(colored('No office to assign!',"red"))
                return (colored('Staff %s has been added successfully!' % (name),"green"))
                
    def assign_random_office(self,name,occupants):
        """Method to randomize office allocation"""
        offices_list = list(self.offices.keys()) #create alist of offices
        checked_offices = [] #store list of offices checked to test if full andassign employee
        while True:
            office = random.choice(list(self.offices))
            if len(self.offices[office]) < occupants:
                self.offices[office].append(name)
                self.rooms[office].append(name)
                print(colored('{} has been assigned office {}!'.format(name,office),"green"))
                break
            if office not in checked_offices:
                checked_offices.append(office)
                if checked_offices == offices_list:
                    print(colored('All offices are full, create a new office before recruiting!',"red"))
                    break
    
    def print_room(self,name):
        """Prints  the names of all the people in room_name on the screen."""
        count=1
        for person in self.rooms[name]:
            print (colored("{}: {}".format(count,person.title()),"cyan"))
            count+=1
        return "EOF List"
        

    
    

   