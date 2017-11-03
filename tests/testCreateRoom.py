import unittest
from models.dojo import Dojo

class TestCreateRoom(unittest.TestCase):
    """create_room command test cases"""
    def setUp(self):
        """create Dojo() object"""
        self.dojo=Dojo()
        
    def test_room_type_can_only_be_office_or_livingspace(self):
        room1=self.dojo.create_room("room1","room")
        error="Only offices and livingspaces allowed!"
        self.assertTrue(error,room1)
        self.assertRaises(RuntimeError, self.dojo.create_room,"room1","room")
        
    
    def test_room_name_only_string(self):
        pass
    
    def test_cannot_create_duplicate_rooms(self):
        pass
    
    def test_room_created_successfully(self):
        pass
    
if __name__ == '__main__':
    unittest.main()