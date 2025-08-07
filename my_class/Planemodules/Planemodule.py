import sys
import os
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Planemodules.Coordinate import PlaneCoordinate

class Plane():
    def __init__(self,id,coordinate:tuple):
        """ID
        coordinate: Class PlaneCoordinate"""
        self.id=id
        self.coordinate=PlaneCoordinate(coordinate) #class coordintae
        self.landing=False
        self.connection=None

    def __str__(self):
        return str([self.id , self.coordinate.coordinates()])

    def move(self,x:tuple=(0,0,0)):
        if len(x) != 3:
            logging.DEBUG("Wrong parametert")
        else: 
            self.coordinate.update(x)



