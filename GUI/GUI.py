import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation
from my_class.Airport.Airportmodule import AirPortPlanes
from my_class.Planemodules import Planemodule

class AirPortGUI:
    def __init__(self,planes=AirPortPlanes):
        self.allplanes=planes
        self.points = np.array([[0,0,0]], dtype=int) # 
        self.labels = ["test"]

        self.fig = plt.figure()
        self.ax = self.fig.add_subplot(111, projection='3d')

        # Scatter plot
        self.scat = self.ax.scatter(
            self.points[:, 0], self.points[:, 1], self.points[:, 2], c='r', s=50
        )

        # # Napisy
        # self.texts = [
        #     self.ax.text(x, y, z, label)
        #     for x, y, z, label in zip(self.points[:, 0], self.points[:, 1], self.points[:, 2], self.labels)
        # ]

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

        self.get_data()
        # Aktualizacja pozycji punktów
        self.scat._offsets3d = (
            self.points[:, 0], self.points[:, 1], self.points[:, 2]
        )

        # Aktualizacja napisów
        for text, (x, y, z) in zip(self.texts, self.points):
            text.set_position((x, y))
      #      text.set_3d_properties(z, zdir='z')

        return self.scat, *self.texts
    
    def get_data(self):
        dummypoints=[]
        self.points = np.array([[0,0,0]], dtype=int) # 
        for key, plane in self.allplanes.planes.items():

            # 1 labes
            self.labels.append(key)
            # 2 add coordinate to np
            new_coordinate=plane.coordinate.get_list_coordinates()
            self.points = np.vstack([
                self.points,new_coordinate])
            
            dummypoints.append(plane.coordinate.get_list_coordinates())

        self.texts = [
        self.ax.text(x, y, z, label)
        for x, y, z, label in zip(self.points[:, 0], self.points[:, 1], self.points[:, 2], self.labels)
        ]
        return self.labels, dummypoints

    def show(self):
        plt.show()

# Uruchomienie
if __name__ == "__main__":
    gui = AirPortGUI()
    gui.show()

