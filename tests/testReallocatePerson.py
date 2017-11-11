"""reallocate person command tests"""
import unittest
from models.dojo import Dojo
from termcolor import colored

class TestReallocatePerson(unittest.TestCase):
    """Reallocation test cases"""
    def setUp(self):
        self.dojo = Dojo()
    def test_person_exists(self):
        """test_person_exists"""
        self.dojo.create_room("red", "office")
        reallocate = self.dojo.reallocate_person("mwenda", "red")
        msg = colored("Person Mwenda does not exist!", "red")
        self.assertEqual(reallocate, msg)
    def test_room_exists(self):
        """test_room_exists"""
        self.dojo.add_person("miriti", 'fellow')
        reallocate = self.dojo.reallocate_person("miriti", "red")
        error = colored("Room red does not exist!", "red")
        self.assertEqual(reallocate, error)
    def test_reallocated(self):
        """test_reallocated successfully"""
        self.dojo.add_person('miriti', 'staff')
        self.dojo.create_room('blue', 'office')
        first = self.dojo.print_room("blue")
        self.assertEqual("0 names printed", first)
        self.dojo.reallocate_person("miriti", "blue")
        results = self.dojo.print_room('blue')
        self.assertEqual(results, "1 names printed") 
