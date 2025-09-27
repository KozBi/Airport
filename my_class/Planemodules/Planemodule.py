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
        self.empy_tank=False


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
        self.landing=False
        self.holding_index=0
        

    def set_target(self,coordintate:tuple,index=None):
        """Set target for a plane"""
        self.target_coordinate.set(coordintate)
        if index is not None:
            self.holding_index=index


    def update_holding_target(self, points):
        """Call when plane reached current target"""
        self.holding_index = (self.holding_index + 1) % len(points)
        self.target = points[self.holding_index]


    def get_target(self):
        target=self.target_coordinate.coordinates()
        return {"target_coordinate": (target)}
    
    def start_landing(self):
        self.landing=True

    def landed(self)->bool:
        """Check if plane hit the finial destination
        Retrun True if plane hit the finial destination"""
        aktual=self.coordinate.coordinates() 
        final_destination=self.selected_runway.coordinate.coordinates()

        if aktual==final_destination:
            return True
        
    def without_target(self):
        return self.target_coordinate.coordinates()==(0,0,0)
    

    def on_target(self):
        if  (self.target_coordinate.width==self.coordinate.width and
            self.target_coordinate.length==self.coordinate.length and
            self.target_coordinate.height==self.coordinate.height):
        #    logging.debug("Plane hit the target")
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
