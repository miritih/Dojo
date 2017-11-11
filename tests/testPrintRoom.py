"""test print room tests"""
import unittest
from models.dojo import Dojo
from termcolor import colored
class TestPrintRoom(unittest.TestCase):
    """testcase for print room"""
    def setUp(self):
        self.dojo = Dojo()   
    def test_print_room(self):
        '''test that members of a room are printed'''
        self.dojo.create_room('blue', 'office')
        self.dojo.add_person('mwenda', 'fellow', 'Y')
        self.dojo.add_person('miriti', 'staff')
        self.dojo.add_person('Eric', 'fellow')
        results = self.dojo.print_room('blue')
        expected = "3 names printed"
        self.assertEqual(results, expected)    
    def test_room_must_be_avialable(self):
        """test that cannot print rooms not available"""
        room = self.dojo.print_room('bluered')
        msg = colored("Room bluered does not exist!", "red")
        self.assertEqual(room, msg)