import sys
import os
import logging
import numpy as np

from my_class import Planemodules
from my_class.Planemodules.Planemodule import PlaneAirport
from my_class.Airport.Area import RunwayArea

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Planemodules.Coordinate import Coordinate

class AirportLandRunway:
    """Single runway that manages a landing queue of planes."""

    def __init__(self, width, length):
        # Queue of planes waiting to land (FIFO order)
        self.queue: list[PlaneAirport] = []

        # Runway starting coordinate
        self.coordinate: Coordinate = Coordinate((width, length, 0))

        # Corridor that leads to the runway
        self.corridor: RunwayArea = RunwayArea(self)

    def start_land(self):
        """Handle landing process for planes in the queue."""

        # If no planes are waiting -> do nothing
        if not self.queue:
            return

        plane = self.queue[0]  # first plane in queue

        # Check if plane has already reached the runway
        if self._plane_hit_runway(plane):
            self.queue.pop(0)  # remove landed plane from the queue

            # If queue is now empty -> nothing else to do
            if not self.queue:
                return

            plane = self.queue[0]  # update current active plane

        # Set target for the first plane
        if self.check_plane_in_corridor(plane):
            # If already in corridor -> direct to runway
            plane.set_target(self.coordinate.coordinates())

            # If another plane is waiting -> direct it to corridor entry
            if len(self.queue) > 1:
                self.queue[1].set_target(self.corridor.start_coordinate())
        else:
            # If not in corridor yet -> send it to corridor entry
            plane.set_target(self.corridor.start_coordinate())

    def _plane_hit_runway(self, plane: PlaneAirport) -> bool:
        """Check if a plane has reached the runway."""
        if plane.coordinate.coordinates() == self.coordinate.coordinates():
            plane.landed()  # mark plane as landed
            return True
        return False

    def add_plane_to_queue(self, plane: PlaneAirport):
        """Add new plane to the landing queue."""
        self.queue.append(plane)

    def __str__(self):
        return f"AiportLandRunway Coordinates {self.coordinate.coordinates()}"
    
    def check_plane_in_corridor(self,plane):
        """Check inf plane cooridor is in cooridor area"""
        return self.corridor.contain(plane.coordinate)
    




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
                runway.add_plane_to_queue(plane)

        for rway in self.runways:
            rway.start_land()

                
    def _select_runway(self,plane:PlaneAirport) -> AirportLandRunway | None:
        plane_pos=plane.coordinate.get_numpy_coordinate()
        # select the closest runway using np.py np.linalg.norm calculate vector norm(lenght)
        return min(self.runways, key=lambda r: np.linalg.norm(plane_pos-r.coordinate.get_numpy_coordinate()))
    