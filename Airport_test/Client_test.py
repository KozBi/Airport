
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Plane.Plane import Plane
from my_class.Plane.PlaneCommandRouter import PlaneCommandRouter




class TestPlaneCommandRouter(unittest.TestCase):

    def setUp(self):
        self.plane = Plane(1, (50,00, 000))
        self.commandrouter = PlaneCommandRouter(self.plane)

    def test_id(self):
        self.assertEqual(self.plane.id, 1)
        
    def test_move(self):    
        while True:
            command={"target_coordinate": (0,0,0)}
            self.commandrouter.command(command)
            print (self.plane.coordinate.coordinates())
            if self.plane.coordinate.coordinates() ==(0,0,0):
                self.assertEqual(self.plane.coordinate.coordinates(), (0,0,0))
                break

if __name__ == '__main__':
    unittest.main()

