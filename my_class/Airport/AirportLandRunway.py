import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Plane.Coordinate import Coordinate

class AirportLandRunway():
    def __init__(self, width, lenght):
        """ width, length - runway starting points"""
        self.width=width
        self.length=lenght
        self.plane_id=None
        self.coordinate=Coordinate((self.width,self.lenght,0))
    
        self.air_coordinate=Coordinate(2000,self.length,2000)

        self.runway_free=True
    # def get_plane(plane-id):
    #     self.