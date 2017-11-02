import unittest
from models.room import Room
class TestCreateRoom(unittest.TestCase):
    def setUp(self):
        self.room=Room()