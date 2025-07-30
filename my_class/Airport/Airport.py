from my_class.Airport.Plane.Plane import Plane
from my_class.Airport.AirportArea import AirportArea
from my_class.Airport.AirportAutopilot import AirportAutopilot
from my_class.Airport.AirportLandRunway import AirportLandRunay

class Airport():
    def __init__(self):
        self.planes={}
        self.airportarea=AirportArea()
        self.airportautopilot=AirportAutopilot()
        self.airportlandrunway=AirportLandRunay()

    def new_plane(self,plane:Plane):
        self.planes[plane.id]=plane

    def remove_plane(self, plane_id):
        self.planes.pop(plane_id,None)

