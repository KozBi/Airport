import sys
import os
import logging
import numpy as np

from my_class import Planemodules
from my_class.Planemodules.Planemodule import PlaneAirport
from my_class.Airport.Area import RunwayArea

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Planemodules.Coordinate import Coordinate

class AirportLandRunway():
    "Single Runway"
    def __init__(self, width, lenght):
        """ width, length - runway starting points"""
        self.planes_to_landrunway:list[PlaneAirport]=[]
        self.coordinate:Coordinate=Coordinate((width,lenght,0))
        self.corridor:RunwayArea=RunwayArea(self)
        self.plane_to_cooridor=None

    def start_land(self):
        if self.plane_to_cooridor is not None or self.plane_to_cooridor.landed():
            try:
                self._add_plane_to_cooridor(self.planes_to_landrunway[0])
                print("Nowy samolot do lawaniwa test test")
            except: pass #no plane
    
    def _add_plane_to_cooridor(self,plane):
        """Select next plane to land"""
        self.planes_to_coordior=plane

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
    """Runways managment class"""
    def __init__(self,airportplanes:AirPortPlanes,runways: list[AirportLandRunway]):
        self.airportplanes=airportplanes
        self.runways=runways

    def start(self):
        for plane in self.airportplanes.planes.values():
            plane:PlaneAirport
            if plane.selected_runway is None:
                runway=plane.selected_runway=self._select_runway(plane) #set runway to the plane
                runway:AirportLandRunway
                runway.add_plane_in_que(plane)

        for rway in self.runways:
            rway.start_land()

       
            
    
    def _select_runway(self,plane:PlaneAirport) -> AirportLandRunway | None:
        plane_pos=plane.coordinate.get_numpy_coordinate()
        # select the closest runway using np.py np.linalg.norm calculate vector norm(lenght)
        return min(self.runways, key=lambda r: np.linalg.norm(plane_pos-r.coordinate.get_numpy_coordinate()))
    