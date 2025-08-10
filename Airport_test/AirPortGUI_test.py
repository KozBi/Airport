
import unittest
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from GUI.GUI import AirPortGUI
from my_class.Planemodules.Planemodule import Plane
from my_class.Airport.Airportmodule import AirPortPlanes


class TestGUI(unittest.TestCase):

    def setUp(self):
        self.plane1=Plane(1,(1000,0,0))
        dummyplanes=[Plane(1,(10000,0,0)),Plane(2,(0,10000,0)),Plane(3,(0,0,5000))]
        self.planes=AirPortPlanes()
        for plane in dummyplanes:
            self.planes.add_plane(plane)

        self.gui=AirPortGUI(self.planes)

    def test_get_data(self):
        result=self.gui.get_data()
        result1=self.gui.allplanes
        print(str(self.plane1))
        print(result)
        print(result1)

    def test_gui(self):
        self.gui.show()
    

