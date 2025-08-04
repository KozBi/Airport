from my_class.Airport.Plane.Coordinate import PlaneCoordinate
import math
#from Coordinate import PlaneCoordinate

class PlaneCommand():
    def __init__(self,crd:PlaneCoordinate):
        self.planecrd=crd #Plane Coordinate


    def move_toward(self, x:int, y:int, z:int , speed:int=10):
        dx=self.planecrd.width - x
        dy=self.planecrd.length - y
        dz=self.planecrd.height - z

        distance = math.hypot(dx, dy,dz)

        while True:

            dx=self.planecrd.width - x
            dy=self.planecrd.length - y
            dz=self.planecrd.height - z

            distance = math.hypot(dx, dy,dz)

            if distance < speed:
                return self.planecrd.coordinates() 
                
                                    
            ux = dx / distance  # unit vector x
            uy = dy / distance  # unit vector y
            uz = dz / distance  # unit vector z

            # self.planecrd.width -= ux * speed
            # self.planecrd.length -= uy * speed
            # self.planecrd.height -= uz * speed
            self.planecrd.update(-ux * speed,-uy * speed,-uz * speed)
            yield self.planecrd.coordinates() 
