import unittest
from models.dojo import Dojo
from termcolor import colored
class TestPrintUnallocated(unittest.TestCase):
    """testcase for print unallocated"""
    def setUp(self):
        self.dojo=Dojo()
        
    def test_print_un_allocated(self):
        '''test_print_un_allocated'''
        self.dojo.create_room('blue', 'office')
        self.dojo.add_person('Ken', 'fellow','Y')
        unallocated=self.dojo.print_unallocated()
        outcome = "1 names printed"
        self.assertEqual(outcome,unallocated)
        
    def test_no_un_allocations(self):
        """test_no_un_allocations"""
        unallocated=self.dojo.print_unallocated()
        msg = colored("No unallocated Employeee at the moment!","red")
        self.assertEqual(unallocated, msg)
        
