import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Planemodules.Planemodule import PlaneAirport
from my_class.Airport.Airportmodule import AirPortPlanes


class TestAirPortPlanes(unittest.TestCase):

    def setUp(self):
        self.dummyplanes=[PlaneAirport(1,(10000,0,0)),PlaneAirport(2,(0,10000,0)),PlaneAirport(3,(0,0,5000))]
     #   self.plane0-=self.dummyplanes[0]
        self.plane1=self.dummyplanes[1]
        self.plane3=self.dummyplanes[2]
        self.planes=AirPortPlanes()
        for plane in self.dummyplanes:
            self.planes.add_plane(plane)


    def test_add_plane(self):
        # test number of planes 
        self.assertEqual(len(self.planes.planes),3)

    def test_remove_plane(self):
        # test number of planes after removing 1 plane 
        self.planes.remove_plane(self.plane3)
        self.assertEqual(len(self.planes.planes),2)
        self.planes.remove_plane(self.plane1)
        self.assertEqual(len(self.planes.planes),1)
        self.planes.remove_plane(self.dummyplanes[0])
        self.assertEqual(len(self.planes.planes),0)

    def test_str_AirportPlanes(self):
        print(self.planes)
