import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from my_class.Planemodules.Planemodule import PlaneAirport
from my_class.Airport.Airportmodule import AirportLandRunway, AirPortPlanes,RouterLandRundway


class AirportAutopilot():
    def __init__(self,planes: AirPortPlanes,runways:RouterLandRundway,):
        self.runways=runways
        self.allplanes=planes

    def start(self):
        # select runway for all planes
        self.runways.start()
        # set a target cooridante for a plane
        for plane in self.allplanes.planes.values():
            plane:PlaneAirport
            if  plane.selected_runway:
                print("test")
                new=plane.selected_runway.coordinate.coordinates()

                # check if plane is already in cooridor
                if plane.selected_runway.plane_to_cooridor:
                    new=plane.selected_runway.corridor.start_coordinate()
                    print("zmienam koordynaty")
            plane.target_coordinate.set(new)



