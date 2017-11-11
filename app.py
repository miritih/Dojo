"""
    Usage:
        create_room <type_room> <room_name>...
        add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
        reallocate_person <person_name> <new_room_name>
        print_allocations [-o=filename]
        print_unallocated [-o=filename]
        print_room <room_name>
        load_people

        dojo (-h | --help | --version)
    Options:
        [wants_accommodation] Y or N
        <type_room>  Type of room to create. only office or livingspace
        <room_name>  Name of room being created
        <person_name> name of employee
        <new_room_name> new room to reallocate
        -o prints output to a file
        -h, --help  Show this screen and exit.
"""

import sys
import cmd
from termcolor import colored
from models.dojo import Dojo
from docopt import docopt, DocoptExit

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    Credit to Docopt doumentation examples.(interactive example)
    """
    def fn(self, arg):
        """decorator function"""
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return
        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return
        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn

class DojoInteractive(cmd.Cmd):
    """dojo intractive """
    intro = colored('Starting Dojo App.....', 'green', attrs=['bold'])
    prompt = colored('DOJO >>>', 'blue', attrs=['bold', 'blink'])
    dojo=Dojo()
    close = sys.stdout
    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>..."""
        for name in args['<room_name>']:
            room=self.dojo.create_room(name, args['<room_type>'])
            print(colored(room[0],room[1], attrs = ['bold']))
    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <person_name> <person_type> [<wants_accommodation>] """
        if arg['<wants_accommodation>'] not in ['y', 'Y', 'YES', 'yes', 'YEAH', 'yeah', None]:
            person = (colored("{} is not a valid paremeter, see help for Usage".format(arg['<wants_accommodation>']), "red"))
        elif arg['<wants_accommodation>'] != None:
            person=self.dojo.add_person(arg['<person_name>'], arg['<person_type>'], arg['<wants_accommodation>'])
        else:
            person = self.dojo.add_person(arg['<person_name>'], arg['<person_type>'])
        print(person)
    @docopt_cmd
    def do_print_room(self, arg):
        """Usage: print_room <room_name> """
        print(colored("Names of all the people in Room "+arg['<room_name>'], "magenta"))
        results = self.dojo.print_room(arg['<room_name>'])
        print(results)       
    @docopt_cmd
    def do_print_allocations(self, arg):
        """Usage: print_allocations [-o]"""
        if arg["-o"]:
            sys.stdout = open("files/allocations.txt", "w")
            self.dojo.print_allocations()
            sys.stdout = self.close
            print(colored('allocations successfully added to file', "green"))
        else:
            print(self.dojo.print_allocations())

    @docopt_cmd
    def do_print_unallocated(self, arg):
        """Usage: print_unallocated [-o] """
        if arg["-o"]:
            sys.stdout = open("files/unallocations.txt", "w")
            self.dojo.print_unallocated()
            sys.stdout = self.close
            print(colored('unallocations successfully added to file', "green"))
        else:
            print(self.dojo.print_unallocated())
    @docopt_cmd
    def do_reallocate_person(self,arg):
        """Usage: reallocate_person <person_name> <new_room_name>"""
        reallocate = self.dojo.reallocate_person(arg['<person_name>'], arg['<new_room_name>'])
        print(reallocate)

    def do_exit(self, arg):
        """Quits out of Interactive Mode."""
        print(colored('Good Bye!', "green"))
        exit()
if __name__ == "__main__":
    print(colored(__doc__, "green"))
    DojoInteractive().cmdloop()
