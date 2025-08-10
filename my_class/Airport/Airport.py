import logging
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Planemodules.Planemodule import Plane
from my_class.Airport.AirportArea import AirportArea
from my_class.Airport.AirportAutopilot import AirportAutopilot
from my_class.Airport.Airportmodule import AirportLandRunway, AirPortPlanes
from my_class.DataBase.DataBaseLog import AirportLogbook
from GUI.GUI import AirPortGUI

DEAFULT_COORDINATE=(1000,1000,5000)

class Airport():
    def __init__(self):
        self.airportarea=AirportArea()
        self.airportplanes=AirPortPlanes()
        self.airportgui=AirPortGUI(self.airportplanes)
      #  self.airportautopilot=AirportAutopilot()
     #   self.airportlandrunway=AirportLandRunway()
        
        self.airportlogbook=AirportLogbook() #create a log 


    
    def get_new_plane(self):
        """Return: Plane object"""
        # 1 create log in database, receive plane id 
        plane_id=self.airportlogbook.connection_established() 
        
        # 2 Create Plane object with ID from Database
        if plane_id is not None:
            plane=Plane(plane_id,DEAFULT_COORDINATE) 
            self.airportplanes.add_plane(plane) 
            return plane
        else:
            logging.debug("Plane cannot be added to Database")

    def remove_plane(self,plane:Plane):
        """Removing a plane from the Airportplanes class"""
        self.airportplanes.remove_plane(plane)


    def start_gui(self):
        """Start a GUI"""
        self.airportgui.show()

