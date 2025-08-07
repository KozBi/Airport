
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Planemodules.Coordinate import PlaneCoordinate

class TestPlaneCoordinate(unittest.TestCase):

    def setUp(self):
        self.crd0=PlaneCoordinate((0,0,0))
        self.crd1=PlaneCoordinate((100,0,0))
        self.crd2=PlaneCoordinate((0,100,0))
        self.crd3=PlaneCoordinate((0,0,100))

    def test_get_list_coordinates(self):
        result=self.crd0.get_list_coordinates()
        self.assertEqual(True,isinstance(result, list))
        
        result=self.crd1.get_list_coordinates()
        self.assertEqual([100,0,0], result)
    