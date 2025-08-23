import unittest
import sys
import os,time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Planemodules.Planemodule import Plane
from my_class.Airport.Area import Area
from my_class.Planemodules.Coordinate import Coordinate


class TestPlane(unittest.TestCase):

    def setUp(self):
        self.plane1=Plane(1,(1000,200,150))
        self.plane2=Plane(2,(1000,190,150))
        self.plane3=Plane(3,(1000,180,0))
        self.plane4=Plane(4,(1000,2000,3000))
        self.start_area=Coordinate((900,200,0))
        self.area=Area(self.start_area,100,-20,200)

    def test_in_area(self):
        result1=self.area.contain(self.plane1.coordinate)
        self.assertTrue(result1)
        result2=self.area.contain(self.plane2.coordinate)
        self.assertTrue(result2)
        result3=self.area.contain(self.plane3.coordinate)
        self.assertTrue(result3)
        result4=self.area.contain(self.plane4.coordinate)
        self.assertFalse(result4)
