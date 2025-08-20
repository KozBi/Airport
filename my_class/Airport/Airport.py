import logging
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from my_class.Planemodules.Planemodule import PlaneAirport

from my_class.Airport.AirportAutopilot import AirportAutopilot
from my_class.Airport.Airportmodule import AirportLandRunway, AirPortPlanes,RouterLandRundway
from my_class.DataBase.DataBaseLog import AirportLogbook
from GUI.GUI import AirPortGUI
from my_class.Airport.Area import AirportArea

class Airport():
    def __init__(self,runways:list[AirportLandRunway]):
        # to do , airportarea send to the GUI INI
        self.airportarea=AirportArea() 
        self.airportplanes=AirPortPlanes()
        self.runways=runways
        self.airportlandrunway=RouterLandRundway(self.airportplanes,self.runways)
        self.airportautopilot=AirportAutopilot(self.airportplanes,self.airportlandrunway)
        self.airportgui=AirPortGUI(self.airportplanes,self.airportautopilot)
        
        self.airportlogbook=AirportLogbook() #create a log 
    
    def get_new_plane(self):
        """Return: Plane object"""
        # 1 create log in database, receive plane id 
        plane_id=self.airportlogbook.connection_established() 
        
        # 2 Create Plane object with ID from Database
        if plane_id is not None:
            plane=PlaneAirport(plane_id) 
            self.airportplanes.add_plane(plane) 
            return plane
        else:
            logging.debug("Plane cannot be added to Database")

    def remove_plane(self,plane:PlaneAirport):
        """Removing a plane from the Airportplanes class"""
        self.airportplanes.remove_plane(plane)


    def start(self):
        """Start a GUI"""
        self.airportgui.show()


