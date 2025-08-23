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
        self.plane_cooridor:PlaneAirport=None
        self.next_plane_cooridor:PlaneAirport=None

    def start_land(self):
        
        # add plane to land
        if len(self.planes_to_landrunway)!=0:
            if self.plane_cooridor is None or self._plane_hit_runway():
                self._add_plane_to_cooridor(self.planes_to_landrunway[0])

        # add next plane to land if plane is nearly to land
        if len(self.planes_to_landrunway)>=2:
            if self.plane_cooridor is None or self.check_plane_in_corridor():
                self._add_next_plane_to_cooridor(self.planes_to_landrunway[1])

        # set final target
        if self.plane_cooridor and self.check_plane_in_corridor():
            self.plane_cooridor.set_target(self.coordinate.coordinates())
            # set next plane to cooridor
            if self.next_plane_cooridor:
                self.next_plane_cooridor.set_target(self.corridor.start_coordinate())
                        
        # set target for coridor
        elif self.plane_cooridor:
            self.plane_cooridor.set_target(self.corridor.start_coordinate())
                        


    def _plane_hit_runway(self):
        """Check if plane is in final destination"""

        if self.plane_cooridor.coordinate.coordinates() == self.coordinate.coordinates():
            print(self.plane_cooridor.coordinate.coordinates())
            print(self.coordinate.coordinates())
            self.plane_cooridor.landed()
            return True
        

    def _add_plane_to_cooridor(self,plane):
        """Select plane to land"""
        self.plane_cooridor=plane


    def _add_next_plane_to_cooridor(self,plane):
        """Select plane to land"""
        self.next_plane_cooridor=plane
        

    def add_plane_in_que(self,plane):
        self.planes_to_landrunway.append(plane)

    def __str__(self):
        return f"AiportLandRunway Coordinates {self.coordinate.coordinates()}"
    
    def check_plane_in_corridor(self):
        """Check inf plane cooridor is in cooridor area"""
        return self.corridor.contain(self.plane_cooridor.coordinate)
    




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
    