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
        self.room_capacity = {}
        self.fellows = [] 
        self.staff = []
        self.rooms = {}
        self.all_employees = []
        self.unallocated = []
        self.accomodated_fellows = []
 
    def create_room(self, name, room_type):
        if not isinstance(name, str):
            return ['Room names can only be strings!', 'red']
        if room_type.lower() not in ['office', 'livingroom']:
            return ['Only offices and livingrooms allowed!', 'red']
        if name in self.rooms:
            return ['Room {} already exists!'.format(name), 'red']
        else:
            class_=getattr(sys.modules[__name__], room_type.capitalize())
            room = class_(name)
            self.rooms[name]=[] #dict of all rooms.
            self.room_capacity[name] = room.capacity
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
        if name.title() in self.all_employees:
            return (colored('oops!! look like someome with this name (%s) alredy exist!' % (name), "red"))
        else:
            name = name.title()
            # append to list of all employees
            self.all_employees.append(name)
            if person_type.lower() == 'fellow':
               # fellow = Fellow(name) #create an instance of Fellow
                self.fellows.append(name) #append to list of all fellows
                if self.offices:
                    # call randomize method
                    self.assign_random_room(name, 6, 'office')
                else:
                    self.unallocated.append(name)
                    print(colored('No office to assign!', "red"))
                if wants_accomodation.lower() in ['y', 'yes', 'yeah'] and self.livingrooms:
                    self.accomodated_fellows.append(name)
                    # call randomize method
                    self.assign_random_room(name, 4, "livingroom")
                else:
                    if name not in self.unallocated:
                        self.unallocated.append(name)
                    print(colored('No Livingroom to assign OR You chose not to be accomodated !', "cyan"))
                return (colored('Fellow %s has been added successfully!' % (name), "green"))
                
            elif person_type.lower() == 'staff':
                if wants_accomodation.lower() in ['y', 'yes', 'yeah']:
                    print(colored('Staff can not be allocated livingrooms!', "red"))
                #staff = Staff(name)
                self.staff.append(name)
                if self.offices:
                    self.assign_random_room(name, 6, 'office') #call assign_random_office
                else:
                    self.unallocated.append(name)
                    print(colored('No office to assign!', "red"))
                return (colored('Staff %s has been added successfully!' % (name), "green"))
                
    def assign_random_room(self,name,occupants,room_type):
        """Method to randomize office allocation."""
        name=name.title()
        callable_ = self.offices if room_type == 'office' else self.livingrooms
        list_ = list(callable_.keys())
        checked = [] #add room here afer each check. to avoid checking same room twice
        while True:
            office = random.choice(list(callable_))
            if len(callable_[office]) < occupants:
                callable_[office].append(name)
                self.rooms[office].append(name)
                print(colored('{} has been assigned {} {}!'.format(name, room_type, office), "green"))
                return False
            if office not in checked:
                checked.append(office)
                if checked == list_:
                    print(colored('All %ss are full at the moment!'%(room_type), "red"))
                    return False
    
    def print_room(self,name):
        """Prints the names of all the people in room_name on the screen."""
        if name not in self.rooms:
            return colored("Room %s does not exist!" % (name), "red")
        count=0
        for person in self.rooms[name]:
            count += 1
            print (colored("{}: {}".format(count,person.title()), "cyan"))
        print("-" * 50)
        return "{} names printed".format(count)

    def print_allocations(self):
        """ Prints a list of allocations onto the screen."""
        if not self.rooms:
            return (colored("No allocations available", "cyan"))
        for room in self.rooms:
            print(room.upper())
            print("-"*50)
            if len(self.rooms[room]) > 0:
                print(', '.join(self.rooms[room]))
            else:
                print("No allocations in this room")
            print("")
        return " "
    
    def print_unallocated(self):
        """Prints the names of all unallocated people."""
        if len(self.unallocated)<=0:
            return colored("No unallocated Employeee at the moment!","red")
        number=0
        for un_allocated in self.unallocated:
            number += 1
            print ("{}: {}".format(number,un_allocated.title()))
        print("-" * 50)
        return ("{} names printed".format(number))

    def reallocate_person(self,name,room_name):
        """reallocate_person"""
        name=name.title()
        if name not in self.all_employees:
            return colored("Person %s does not exist!" % (name), "red")
        if room_name not in self.rooms:
            return colored("Room %s does not exist!" % (room_name), "red")
        if name in self.rooms[room_name]:
            return colored("person %s already assigned room %s" % (name, room_name), "red")
        capacity = self.room_capacity[room_name]
        if len(self.rooms[room_name]) >= capacity:
           return colored("Opps! Room %s is fully packed!" % (room_name), "red")
        print(colored("Removing %s from current room if assigned any" % (name), "cyan"))
        #remove name from current room
        [self.rooms[room].remove(person) for room in self.rooms for person in self.rooms[room] if person == name]
        #remove name from unallocated if prevously unllocated
        if name in self.unallocated:
            self.unallocated.remove(name)
        print(colored("assigning %s new room %s" % (name,room_name), "cyan"))
        self.rooms[room_name].append(name)
        return (colored("Employee %s successfully reallocated to room %s!" % (name, room_name), "green"))

    def load_people(self):
        """load_people"""
        file = open("files/load_people.txt", "r")
        count=0
        for line in file:
            count+=1
            person = line.split()
            if len(person) == 3:
                self.add_person(person[0],person[1],person[2])
                print(colored(colored('%s %s has been added successfully!' % (person[1],person[0]), "green")))
            else:
                self.add_person(person[0], person[1])
                print(colored(colored('%s %s has been added successfully!' %(person[1], person[0]), "green")))
        file.close
        return (colored("%s people successfuly loaded from file" % (count), "green", attrs=["bold"]))
