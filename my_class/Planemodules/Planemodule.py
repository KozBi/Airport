import sys
import os
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Planemodules.Coordinate import PlaneCoordinate
#from my_class.Airport.Airportmodule import AirportLandRunway, AirPortPlanes

class Plane():
    def __init__(self,id,coordinate:tuple=(0,0,0)):
        """ID
        coordinate: Class PlaneCoordinate"""
        self.id=id
        self.coordinate=PlaneCoordinate(coordinate) #class coordintae
        self.connection=None


    def __str__(self):
        return str([self.id , self.coordinate.coordinates()])

    def move(self,x:tuple=(0,0,0)):
        if len(x) != 3:
            logging.DEBUG("Wrong parameteters")
        else: 
            self.coordinate.update(x)

class PlaneAirport(Plane):

    def __init__(self,id,coordinate:tuple=(0,0,0)):
        """ID
        coordinate: Class PlaneCoordinate"""
        super().__init__(id,coordinate)
        
        self.selected_runway=None #class runway that already selected
        self.target_coordinate=PlaneCoordinate(coordinate)

    def get_target(self):
        target=self.target_coordinate.coordinates()
        return {"target_coordinate": (target)}

