
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Planemodules.Planemodule import Plane
from my_class.Planemodules.PlaneCommandRouter import PlaneCommandRouter




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

    def test_change_cord_target(self):
        i=0
        while True:            
            if i < 5:
                command={"target_coordinate": (0,100,0)}
            else:
                #change destination after few steps
                command={"target_coordinate": (100,0,0)}

            self.commandrouter.command(command)
            print (self.plane.coordinate.coordinates())

            if self.plane.coordinate.coordinates() ==(100,000,0):
                self.assertEqual(self.plane.coordinate.coordinates(), (100,0,0))
                break
            i+=1

            if i>200:
                #something goes wrong
                self.assertIn(False)
                break
            

if __name__ == '__main__':
    unittest.main()

