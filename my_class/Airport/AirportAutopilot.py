import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from my_class.Planemodules.Planemodule import PlaneAirport
from my_class.Airport.Airportmodule import AirportLandRunway, AirPortPlanes,RouterLandRundway


class AirportAutopilot():
    def __init__(self,runways:RouterLandRundway,planes: AirPortPlanes):
        self.runways=runways
        self.allplanes=planes

#     def _plane_is_in_corridor(self,airportlandrunway:AirportLandRunway,plane:Plane) -> bool:
#         """
# Checks if the aircraft is exactly at the landing runway coordinates.
#         """
#         return plane.planecoordinate.coordinate == airportlandrunway.coordinate

#     def auto_landing(self,airportlandrunway:AirportLandRunway,plane:Plane):
#         while not self._plane_is_in_corridor(airportlandrunway,plane):
#             pass

    def start(self):
        # select runway for all planes
        self.runways.select_runway()
        # set a target cooridante for a plane
        for plane in self.allplanes:
            plane:PlaneAirport
            plane.target_coordinate.set=plane.selected_runway.coordinate.coordinates()



