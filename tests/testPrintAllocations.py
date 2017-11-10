import unittest
from models.dojo import Dojo
from termcolor import colored

class TestPrintAllocations(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()
        
    def test_no_allocations_available(self):
        msg=colored("No allocations available","cyan")
        allocations=self.dojo.print_allocations()
        self.assertEqual(msg,allocations)
       
        
        
    
