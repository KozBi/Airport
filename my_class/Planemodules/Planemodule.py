import sys,time
import os
import logging


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Planemodules.Coordinate import PlaneCoordinate

class Plane():
    def __init__(self,id,coordinate:tuple=(0,0,0)):
        """Base class for a Plane Server/Client"""
        self.id=id
        self.coordinate=PlaneCoordinate(coordinate) #class coordintae
        self.connection=None
        self.fuel=None


    def __str__(self):
        return str([self.id , self.coordinate.coordinates()])
    
    def move(self,x:tuple=(0,0,0)):
        if len(x) != 3:
            logging.DEBUG("Wrong parameteters")
        else: 
            self.coordinate.update(x)

class PlaneAirport(Plane):

    def __init__(self,id,coordinate:tuple=(0,0,0)):
        """Class Plane for Server site"""
        super().__init__(id,coordinate)
        
        self.selected_runway=None #class runway that already selected
        self.target_coordinate=PlaneCoordinate(coordinate)

    def set_target(self,coordintate:tuple):
        """Set target for a plane"""
        self.target_coordinate.set(coordintate)

    def get_target(self):
        target=self.target_coordinate.coordinates()
        return {"target_coordinate": (target)}

    def landed(self):
        """Check if plane hit the finial destination"""
        aktual=self.coordinate.coordinates() 
        final_destination=self.selected_runway.coordinate.coordinates()

        if aktual==final_destination:
            return True
        
class PlaneClinet(Plane):

    def __init__(self,id,coordinate:tuple=(0,0,0)):
        """Class Plane for Clinet site"""
        super().__init__(id,coordinate)

        self.start_time=time.time()
        self.fuel=3*3600 # 3h
      #  self.fuel=3*2 # 3h

    def fuel_check(self) -> bool: 
        """Calculate fuel and return True if a tank ist empty"""
        # 1 set a time
        now=time.time()
        # 2 calcute difference in seconds
        elapsed=now - self.start_time 
        # substract from fuel seconds that has passed
        self.fuel=self.fuel-elapsed
        self.start_time =time.time()

        if self.fuel<=0:
            self.fuel=0
            return True
