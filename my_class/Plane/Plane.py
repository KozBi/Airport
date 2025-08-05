import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Plane.Coordinate import PlaneCoordinate
class Plane():
    def __init__(self,id,coordinate:tuple):
        """ID"""
        self.id=id
        self.coordinate=PlaneCoordinate(coordinate)
        self.landing=False
        self.connection=None



