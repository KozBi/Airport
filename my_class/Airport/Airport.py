import logging
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Plane.Plane import Plane
from my_class.Airport.AirportArea import AirportArea
from my_class.Airport.AirportAutopilot import AirportAutopilot
from my_class.Airport.AirportLandRunway import AirportLandRunway
from my_class.DataBase.DataBaseLog import AirportLogbook

DEAFULT_COORDINATE=(1000,1000,5000)

class Airport():
    def __init__(self):
        self.planes={}
        self.airportarea=AirportArea()
      #  self.airportautopilot=AirportAutopilot()
     #   self.airportlandrunway=AirportLandRunway()

        self.airportlogbook=AirportLogbook() #create a log 


    def _new_plane(self,plane:Plane):
         self.planes[plane.id]=plane

    def remove_plane(self, plane_id):
        self.planes.pop(plane_id,None)

    
    def get_new_plane(self):
        """Return: Plane object"""
        plane_id=self.airportlogbook.connection_established() #create log in database, receive plane id 
        
        if plane_id is not None:
            plane=Plane(plane_id,DEAFULT_COORDINATE) #create Plane
            self._new_plane(plane) #add plane to the airport class
            return plane
        else:
            logging.debug("Plane cannot be added to Database")

