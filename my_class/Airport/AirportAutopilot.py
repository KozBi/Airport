import sys
import os
import logging,math

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from my_class.Planemodules.Planemodule import PlaneAirport
from my_class.Airport.Airportmodule import AirportLandRunway, AirPortPlanes,RouterLandRundway
from my_class.DataBase.DataBaseLog import AirportLogbook

class Autopilot():
    def __init__(self,planes: AirPortPlanes,runways:RouterLandRundway,airportlogbook=None):
        self.runways=runways
        self.allplanes=planes
        self.airportlogbook=airportlogbook #
        self.positions=((1000,1000))
        self._counter=0
        self._x=(2000,4000,6000,8000,8000,
                 8000,4000,2000,2000,2000)
        self._y=(8000,6000,4000,2000,2000,
                 2000,4000,6000,8000,8000)

    def start(self):
        # select runway for all planes
        self.runways.start()
        self.run_planes()
        # if airportlogbook not provieded skipp method - it's optional
        if self.airportlogbook:
            self.airportlogbook.check_collision()
        # set a target cooridante for a plane

    
    def run_planes(self):
        height=1000
        for runway in self.runways.runways:
            height+=500
            runway:AirportLandRunway
            # check if there are planes in que without target destination
            if len(runway.queue)>2:
                
                for plane in runway.queue[2:]:
                    # check if new coordinate needed
                    if plane.without_target() or  plane.on_target():
                        self.set_new_positions()
                    # set a new coordinate for all planes
                    else:# plane.without_target() or plane.on_target():
                        continue
                        

    def set_new_positions(self):
        """Assign holding pattern coordinates for planes beyond first 2 in queue."""
        
        base_height = 1500
        max_heith=5000
        vertical_step = (max_heith-base_height)/100 #5000-1500/100 = 35
        radius = 1500  # promień krążenia
        angle_step = 15  # stopnie między samolotami
        
        for r_idx, runway in enumerate(self.runways.runways):
            if len(runway.queue)>0:
                vertical_step = (max_heith-base_height)/len(runway.queue)
            runway_base_height = base_height + r_idx * vertical_step
            
            for p_idx, plane in enumerate(runway.queue):
                if plane.landing:
                    continue
                
                # wysokość samolotu w holding pattern
                z = runway_base_height + p_idx * vertical_step
                
                # kąt w okręgu (cyklicznie)
                if not hasattr(plane, 'angle'):
                    plane.angle = 0
                
                x = runway.corridor.start_coordinate()[0] + radius * math.cos(math.radians(plane.angle))
                y = runway.corridor.start_coordinate()[1] + radius * math.sin(math.radians(plane.angle))
                
                plane.set_target((x, y, z))
                
                # przesunięcie kąta dla płynnego ruchu w kolejnej iteracji
                plane.angle = (plane.angle + angle_step) % 360





