import sys
import os
import logging

from my_class import Planemodules
from my_class.Planemodules.Planemodule import PlaneAirport

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Planemodules.Coordinate import Coordinate

class AirportLandRunway():
    def __init__(self, width, lenght):
        """ width, length - runway starting points"""
        self.planes_to_landrunway:list[PlaneAirport]=[]
        self.coordinate=Coordinate((width,lenght,0))
    
    def add_plane_in_que(self,plane):
        self.planes_to_landrunway.append(plane)

    def __str__(self):
        return f"AiportLandRunway Coordinates {self.coordinate.coordinates()}"



class AirPortPlanes():
    def __init__(self):
        """Contain all planes in a dict"""
        self.planes={}

    def __str__(self):
        return str(self.planes)

    def add_plane(self, plane:PlaneAirport):
        """Add a plane to the list"""
        if type(plane)==PlaneAirport:
            self.planes[plane.id]=plane
        else:
            logging.debug("Wrong class as asrgument")

    def remove_plane(self, plane:PlaneAirport):
        """Remove a plane from the list"""
        if type(plane)==PlaneAirport:
            key=plane.id
            self.planes.pop(key,True)
            logging.info(f"Plane {plane.id} has been removed")
        else:
            logging.debug("Wrong class as asrgument")

class RouterLandRundway():
    def __init__(self,airportplanes:AirPortPlanes,runways: list[AirportLandRunway]):
        self.airportplanes=airportplanes
        self.runways=runways

    def start(self):
        for plane in self.airportplanes.planes.values():
            plane:PlaneAirport
            if not plane.selected_runway:
                runway=plane.selected_runway=self._select_runway() #set runway to the plane
                runway:AirportLandRunway
                runway.add_plane_in_que(plane)
            
    
    def _select_runway(self) -> AirportLandRunway | None:
        if not self.runways:
            return None
        # find runway with minimal numer of planes.
        return min(self.runways, key=lambda r: len(r.planes_to_landrunway))
