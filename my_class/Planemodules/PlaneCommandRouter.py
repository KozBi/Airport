import sys
import os
import math
from copy import deepcopy

import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Planemodules.Coordinate import PlaneCoordinate, Coordinate
from my_class.Planemodules.Planemodule import PlaneClinet

class PlaneCommandRouter():
    def __init__(self,plane:PlaneClinet):
        self.plane=plane
        self.planecommand=PlaneCommand(self.plane.coordinate)
        self._target_coordinate=PlaneCoordinate() #dummy target coordinate to not create all the time a new object
        self.dissconect=False 

    def handle_command(self,command:dict):
        if command.get("target_coordinate"):
            self.coordinate_target=command["target_coordinate"]
            # 1. set a new coordianate 2. call move_toward
            self._target_coordinate.set(self.coordinate_target)
            self.planecommand.move_toward(self._target_coordinate)
        
        if "release_disc" in command and command["release_disc"]:
            self.dissconect = True

        if "release" in command and command["release"]==False:
            print("No release to connect to Airport")
            self.dissconect = True
        

    def answer(self):
        # wysylac caly czas koordynaty.. Chyba ze cos innego wtedy if i podmienic komende.
        sendjson={
        "type": "position_update",
        "position": [self.plane.coordinate.width, self.plane.coordinate.length, self.plane.coordinate.height],
        "fuel" : self.plane.fuel

        }
        # check if tank is not empty
        if self.plane.fuel_check():
            sendjson={
            "type": "colission",
            "reason":"Out of fuel"
            }
          #  self.dissconect=True
        return (json.dumps(sendjson).encode('utf-8'))

class PlaneCommand():
    def __init__(self,crd:PlaneCoordinate):

        self.planecrd=crd #Plane Coordinate
        self.dummy_planecrd=deepcopy(crd) #Plane Coordinate
        self.generator=None
        self.finial_crd=None


    def move_toward(self, crd:Coordinate , speed:int=70):
        speed=200
        # this function do generator if is called once again generator is changed
        if self.generator is None or self.finial_crd != crd:
            self.finial_crd = crd
            self.generator=self.move_toward_generator(crd,speed) #instead of new threat, python do everthing and make genetator to work with loop and sleep.
        try:
            new_coord=next(self.generator)
            self.planecrd.set(new_coord)
        except StopIteration:
            self.generator=None


    def move_toward_generator(self, crd:Coordinate , speed:int):
        """crd - target coordingate
            Return generator of coordinates - it is a path to the destination"""
        dx=self.dummy_planecrd.width - crd.width
        dy=self.dummy_planecrd.length - crd.length
        dz=self.dummy_planecrd.height - crd.height
        self.finial_crd=crd

        while True:

            dx=self.dummy_planecrd.width - crd.width
            dy=self.dummy_planecrd.length - crd.length
            dz=self.dummy_planecrd.height - crd.height

            distance = math.hypot(dx, dy, dz)                
                                    
            ux = dx / distance  # unit vector x
            uy = dy / distance  # unit vector y
            uz = dz / distance  # unit vector z

            self.dummy_planecrd.update((-ux * speed,-uy * speed,-uz * speed))
            if distance >= speed:
                #generate value for generator
                yield self.dummy_planecrd.coordinates() 
            else: 
                # if disstance lower than speed yield last value - target value
                yield self.finial_crd.coordinates()
                return

