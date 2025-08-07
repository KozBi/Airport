import sys
import os
from my_class import Planemodules

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Planemodules.Coordinate import Coordinate

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

class AirPortPlanes():
    def __init__(self):
        """Contain all planes in a dict"""
        self.planes={}

    def __str__(self):
        return str(self.planes)

    def add_plane(self, plane:Planemodules):
        self.planes[plane.id]=plane

    def remove_plane(self, plane_id):
        self.planes.pop(plane_id,None)

    
        
