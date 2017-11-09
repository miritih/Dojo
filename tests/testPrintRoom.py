import unittest
from models.dojo import Dojo
class TestPrintRoom(unittest.TestCase):
    """testcase for print room"""
    def setUp(self):
        self.dojo=Dojo()
        
    def test_print_room(self):
        '''test that members of a room are printed'''
        self.dojo.create_room('blue', 'office')
        self.dojo.create_room('brown', 'livingspace')
        self.dojo.add_person('mwenda', 'fellow','Y')
        self.dojo.add_person('miriti', 'staff')
        self.dojo.add_person('Eric', 'fellow')
        self.dojo.print_room('blue')