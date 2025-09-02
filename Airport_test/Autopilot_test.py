
import unittest
import sys
import os,time

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Airport.Airportmodule import AirPortPlanes, AirportLandRunway , RouterLandRundway
from my_class.Airport.Airportmodule import AirportLandRunway, AirPortPlanes,RouterLandRundway
from my_class.Planemodules.Planemodule import PlaneAirport
from my_class.Airport.AirportAutopilot import Autopilot

class Testautopilot(unittest.TestCase):

    def setUp(self):
        self.dummyplanes=[PlaneAirport(1,(1700,2000,0)),
                          PlaneAirport(2,(7000,2000,0)),
                          PlaneAirport(3,(9000,3000,5000))
                         ,PlaneAirport(4,(8000,0000,0000))] #plane 4 is alredy in runway1
        self.dummyplane0:PlaneAirport=self.dummyplanes[0]
        self.dummyplane1:PlaneAirport=self.dummyplanes[1]
        self.dummyplane2:PlaneAirport=self.dummyplanes[2]
        self.dummyplane3:PlaneAirport=self.dummyplanes[3]
        self.runway1=AirportLandRunway(2000,3000)
        self.planes=AirPortPlanes()
        self.router=RouterLandRundway(self.planes,[self.runway1])
        self.autopilot=Autopilot(self.planes,self.router)
        # add planes
        for plane in self.dummyplanes:
            self.planes.add_plane(plane)

        # select runway
        self.router.start()
        

    def test_lengh_of_list(self):
        #all planes are added to ranway
        self.autopilot.start()
        result1=self.runway1.planes_to_landrunway
        self.assertEqual(self.dummyplanes,result1)

    def test_move_to_coordinor(self):
        
        self.autopilot.start()

        #check if plane has finial coordinate
        result1=self.dummyplane0.target_coordinate.coordinates()
        tup=(2000,3000,0)
        self.assertEqual(result1,tup)
        #check if plane is in corridor
        result2=self.runway1.check_plane_in_corridor()
        self.assertTrue(result2)

    def test_next_planemove_to_coordinor(self):
        
        self.autopilot.start()

        #check if plane 2 is selected 
        result1=self.runway1.next_plane_cooridor
        self.assertEqual(result1,self.dummyplane1)

        # #check if plane 2 has right coordinate
        result2=self.dummyplane1.target_coordinate.coordinates()
        tup=self.runway1.corridor.start_coordinate()
        self.assertEqual(result2,tup)

    def testautopilot(self):
        self.autopilot.set_new_positions()
        print(self.dummyplane2.target_coordinate)
        print(self.dummyplane3.target_coordinate)


    

  

    # def test_move_coordidor_runway(self):
    #     self.autopilot.start()
    #     result1=self.dummyplanes0.target_coordinate
    #     print(result1)
        