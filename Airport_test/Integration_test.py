
import unittest
import sys
import os

#from my_class.ServerConnection import ServerConnetions
#from my_class.Airport.Airport import Airport

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Airport.Airportmodule import AirPortPlanes, AirportLandRunway , RouterLandRundway
from my_class.Airport.AirportAutopilot import AirportAutopilot
from my_class.Planemodules.Planemodule import PlaneAirport


class TestAirPortRouter(unittest.TestCase):

    def setUp(self):
        self.dummyplanes=[PlaneAirport(1,(10000,2000,0)),PlaneAirport(2,(1000,20000,0)),PlaneAirport(3,(9000,3000,5000))]
        self.dummyplanes0=self.dummyplanes[0]
        self.dummyplanes1=self.dummyplanes[1]
        self.dummyplanes2=self.dummyplanes[2]
        self.runway1=AirportLandRunway(8000,0000)
        self.runway2=AirportLandRunway(2000,0000)
        self.planes=AirPortPlanes()
        self.router=RouterLandRundway(self.planes,[self.runway1,self.runway2])
        self.autopilot=AirportAutopilot(self.planes,self.router)
        for plane in self.dummyplanes:
            self.planes.add_plane(plane)

    def test_number_of_landrundway(self):
        # 
        result=len(self.router.runways)
        self.assertEqual(2, result)

    def test_selection_of_runway(self):
        self.router.start()
        result1=self.dummyplanes0.selected_runway
        result2=self.dummyplanes1.selected_runway
        result3=self.dummyplanes2.selected_runway
        print(str(result1))
        self.assertIn(result1,[self.runway1,self.runway2])
        self.assertIn(result2,[self.runway1,self.runway2])
        self.assertIn(result3,[self.runway1,self.runway2])
        self.assertIn(result1,[self.runway1,0])
        self.assertIn(result2,[self.runway2,0])
        self.assertIn(result3,[self.runway1,0])

    def test_autopilot(self):
        self.autopilot.start()
        result1=self.dummyplanes0.target_coordinate.coordinates()
        result2=self.dummyplanes1.target_coordinate.coordinates()
        result3=self.dummyplanes2.target_coordinate.coordinates()
        # plane targer are the same like the runway 1 or 2
        self.assertIn(result1,[self.runway1.coordinate.coordinates(),self.runway2.coordinate.coordinates()])
        self.assertIn(result2,[self.runway1.coordinate.coordinates(),self.runway2.coordinate.coordinates()])
        self.assertIn(result3,[self.runway1.coordinate.coordinates(),self.runway2.coordinate.coordinates()])



