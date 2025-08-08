import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from my_class.Airport.Airportmodule import AirPortPlanes
from my_class.Planemodules.Planemodule import Plane
import time
import logging

class AirPortGUI:
    def __init__(self,planes=AirPortPlanes):
        self.allplanes:AirPortPlanes=planes
        self.points = []
        self.labels = []
        self.texts = []

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

        # Scatter plot
        self.scat = self.ax.scatter(
            [], [], [], c='r', s=50)

        # Ograniczenia osi
        self.ax.set_xlim(0, 10000)
        self.ax.set_ylim(0, 10000)
        self.ax.set_zlim(0, 5000)
        self.ax.set_xlabel('X')
        self.ax.set_ylabel('Y')
        self.ax.set_zlabel('Z')
        self.ax.set_title('Airport 3D')

        # Animacja
        self.ani = FuncAnimation(self.fig, self._update, frames=200, interval=50, blit=False)

    def _update(self,frame):
       

        for plane in self.allplanes.planes.values():
            print(plane.coordinate.coordinates())
            print("movment")

        1 # Initializate data
        self.points = []
        self.labels = []

        for key, plane in self.allplanes.planes.items():
            # 2 labes
            self.labels.append(key)
            # 3 add coordinate to np
            new_coordinate=plane.coordinate.get_list_coordinates()
            self.points.append(new_coordinate)

        if len(self.points)==0: ###
            logging.info("Nothing is happening")
            return  # Return None if no client - Plane is connected

        self.points = np.array(self.points)
        
        # Aktualizacja pozycji punktów
        self.scat._offsets3d = (
            self.points[:, 0], self.points[:, 1], self.points[:, 2]
        )
        
        # Usuń stare napisy
        for t in self.texts:
            t.remove()
        self.texts = []

        # Dodaj nowe napisy
        for (x, y, z), label in zip(self.points, self.labels):
            self.texts.append(self.ax.text(x, y, z, label))



        return self.scat, *self.texts
    

    def show(self):
        plt.show()

# Uruchomienie
if __name__ == "__main__":
    gui = AirPortGUI()
    gui.show()

