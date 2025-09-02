import sys, os

from my_class.Planemodules.Coordinate import Coordinate
#from my_class.Airport.Airportmodule import AirportLandRunway

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class Area():
    """Base class"""
    def __init__(self,coordinate:Coordinate,width,length, height):
        self.s_x=coordinate.width #start x 
        self.s_y=coordinate.length #start y 
        self.s_z=coordinate.height #start z 
        self.e_x=coordinate.width + width #end x 
        self.e_y=coordinate.length + length #end y 
        self.e_z=coordinate.height +height #end z 

        # always min -> max
        self.min_x, self.max_x = sorted([self.s_x, self.e_x])
        self.min_y, self.max_y = sorted([self.s_y, self.e_y])
        self.min_z, self.max_z = sorted([self.s_z, self.e_z])

    def contain(self, coordinate: "Coordinate") -> bool:
        """Check if coordinate are inside Area"""
        return (
            self.min_x <= coordinate.width  <= self.max_x and
            self.min_y <= coordinate.length <= self.max_y and
            self.min_z <= coordinate.height <= self.max_z
        )

class AirportArea(Area):
    def __init__(self,width=10000,length=10000, height=5000):
        coordinate=Coordinate()
        super().__init__(coordinate,width,length,height)


class RunwayArea(Area):
    def __init__(self,runway,width=-300,length=-2500):
        height=600
        runway=(runway.coordinate)
        super().__init__(runway,width,length,height)   
        
    def start_coordinate(self) -> tuple: 
        """Return tuple (width,lenght,height)"""
        return (self.e_x,self.e_y,self.e_z)
    