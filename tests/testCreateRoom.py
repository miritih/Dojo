import unittest
from models.dojo import Dojo

class TestCreateRoom(unittest.TestCase):
    """create_room command test cases"""
    def setUp(self):
        """create Dojo() object"""
        self.dojo=Dojo()
        
    def test_room_type_can_only_be_office_or_livingspace(self):
        room1=self.dojo.create_room("room1","room")
        error="Only offices and livingrooms allowed!"
        self.assertEqual(error,room1[0])
        
    
    def test_room_name_only_string(self):
        room2=self.dojo.create_room(1212,1212)
        err='names and person type should be a strings!'
        self.assertTrue(err,room2[0])
    
    def test_cannot_create_duplicate_rooms(self):
        room=self.dojo.create_room("stive", "office")
        dup=self.dojo.create_room("stive", "office")
        err= "Room stive already exists!"
        self.assertEqual(err,dup[0])

    def test_room_created_successfully(self): 
        initial_room_count = len(self.dojo.rooms)
        blue_office = self.dojo.create_room("Blue", "office")
        self.assertTrue(blue_office)
        new_room_count = len(self.dojo.rooms)
        self.assertEqual(new_room_count - initial_room_count, 1)
      
    
if __name__ == '__main__':
    unittest.main()