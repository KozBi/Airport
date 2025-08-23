import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from my_class.Planemodules.Planemodule import PlaneAirport
from my_class.Airport.Airportmodule import AirportLandRunway, AirPortPlanes,RouterLandRundway


class Autopilot():
    def __init__(self,planes: AirPortPlanes,runways:RouterLandRundway,):
        self.runways=runways
        self.allplanes=planes

    def start(self):
        # select runway for all planes
        self.runways.start()
        # set a target cooridante for a plane


    


    def run_planes(self):
        pass
            # for plane in self.allplanes.planes.values():
            #     plane:PlaneAirport
                
            #     #  new=plane.selected_runway.coordinate.coordinates()
            #     if  plane.selected_runway:
            #         # if plane has destitatnion a cooridor set a target
            #         if plane.selected_runway.

            #         if plane.selected_runway.plane_cooridor:
            #             new=plane.selected_runway.corridor.start_coordinate()

            #             #if plane is alraedy in cooridot set a final tartger
            #             if plane.selected_runway.check_plane_in_corridor():
            #                 new=plane.selected_runway.coordinate.coordinates()
                    
                            
            #     plane.set_target(new)



