
import unittest
import sys
import os,time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Planemodules.Planemodule import Plane,PlaneClinet


class TestPlane(unittest.TestCase):

    def setUp(self):
        self.plane1=Plane(1,(1000,0,0))
        self.plane2=Plane(2,(1000,0,0))
        self.plane3=Plane(3,(1000,0,0))
        self.plane4=Plane(4,(1000,0,0))

        self.clientplane1=PlaneClinet(5,(1000,0,0))

    def test_move(self):
        result1=self.plane1.coordinate.coordinates()
        self.assertEqual(result1, (1000,0,0))

        # move plane
        self.plane1.move((0,1000,0))
        result2=self.plane1.coordinate.coordinates()
        self.assertEqual(result2, (1000,1000,0))

    def test_fuelcheck(self):
        time.sleep(1)
        self.clientplane1.fuel_check()
        result=self.clientplane1.fuel
        self.assertNotEqual(result,10800)
        
        time.sleep(1)
        self.clientplane1.fuel_check()
        result=self.clientplane1.fuel
        self.assertLess(result,10798)