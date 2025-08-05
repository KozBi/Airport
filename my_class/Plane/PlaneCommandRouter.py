import sys
import os
import math
from copy import deepcopy

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Plane.Coordinate import PlaneCoordinate, Coordinate
from my_class.Plane.Plane import Plane

class PlaneCommandRouter():
    def __init__(self,plane:Plane):
        self.plane=plane
        self.planecommand=PlaneCommand(self.plane.coordinate)


    def command(self,command:dict):
        if command.get("target_coordinate"):
            self.coordinate_target=command.get("target_coordinate")
            self.planecommand.move_toward(Coordinate(self.coordinate_target))
   

class PlaneCommand():
    def __init__(self,crd:PlaneCoordinate):

        self.planecrd=crd #Plane Coordinate
        self.dummy_planecrd=deepcopy(crd) #Plane Coordinate
        self.generator=None
        self.finial_crd=None
        print(self.dummy_planecrd)


    def move_toward(self, crd:Coordinate , speed:int=10):
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
            print(self.dummy_planecrd)
            if distance >= speed:
                #generate value for generator
                yield self.dummy_planecrd.coordinates() 
            else: 
                # if disstance lower than speed yield last value - target value
                yield self.finial_crd.coordinates()
                return

