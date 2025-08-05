import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from my_class.Plane.Plane import Plane
from my_class.Airport.AirportLandRunway import AirportLandRunway
from my_class.Airport.AirportArea import AirportArea


class AirportAutopilot():
    def __init__(self,airportarea:AirportArea,list_landrunway:list,planes:dict):
        self.airportarea=airportarea
        self.landrunways=list_landrunway
        self.planes=planes

    def _plane_is_in_corridor(self,airportlandrunway:AirportLandRunway,plane:Plane) -> bool:
        """
Checks if the aircraft is exactly at the landing runway coordinates.
        """
        return plane.planecoordinate.coordinate == airportlandrunway.coordinate

    def auto_landing(self,airportlandrunway:AirportLandRunway,plane:Plane):
        while not self._plane_is_in_corridor(airportlandrunway,plane):
            pass
