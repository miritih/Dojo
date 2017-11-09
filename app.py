"""
    Usage:
        create_room <type_room> <room_name>...
        add_person <person_name> <FELLOW|STAFF> [wants_accommodation]
        dojo (-h | --help | --version)
    Options:
        type_room  Type of room to create. only office or livingspace
        room_name  Name of room being created
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
    intro = colored('Starting Dojo App.....', 'green', attrs=['bold'])
    prompt = colored('DOJO >>>', 'blue', attrs=['bold','blink'])
    dojo=Dojo()
   
    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room <room_type> <room_name>..."""
        for name in args['<room_name>']:
            room=self.dojo.create_room(name,args['<room_type>'])
            print(colored(room[0],room[1], attrs=['bold']))

    @docopt_cmd
    def do_add_person(self, arg):
        """Usage: add_person <person_name> <person_type> [<wants_accommodation>] """
       
        if arg['<wants_accommodation>'] != None:
            person=self.dojo.add_person(arg['<person_name>'],arg['<person_type>'],arg['<wants_accommodation>'])
        else:
            person=self.dojo.add_person(arg['<person_name>'],arg['<person_type>'])
        print(person)

    def do_exit(self, arg):
        """Quits out of Interactive Mode."""
        print('Good Bye!')
        exit()

if __name__=="__main__":
    print(colored(__doc__,"green"))
    DojoInteractive().cmdloop()