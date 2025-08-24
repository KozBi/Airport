import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from my_class.Planemodules.Planemodule import PlaneAirport
from my_class.Airport.Airportmodule import AirportLandRunway, AirPortPlanes,RouterLandRundway


class Autopilot():
    def __init__(self,planes: AirPortPlanes,runways:RouterLandRundway,):
        self.runways=runways
        self.allplanes=planes
        self.positions=((1000,1000))
        self._counter=0
        self._x=(2000,4000,6000,8000,8000,
                 8000,4000,2000,2000,2000)
        self._y=(8000,6000,4000,2000,2000,
                 2000,4000,6000,8000,8000)

    def start(self):
        # select runway for all planes
        self.runways.start()
        # set a target cooridante for a plane

    
    def run_planes(self):
        height=1000
        for runway in self.runways:
            height+=500
            runway:AirportLandRunway
            # check if there are planes in que without target destination
            if len(runway.queue)>2:
                
                for plane in runway.queue[2:]:
                    # check if new coordinate needed
                    if not (plane.without_target() or plane.on_target()):
                        return
                    elif plane.without_target():
                        self.set_new_positions()
                        pass

    def set_new_positions(self):
        height=2000
        for runway in self.runways:
            for index, plane in enumerate(runway.queue[2:]):
                plane:PlaneAirport
                







