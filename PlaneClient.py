import socket
import json
from my_class.Plane.Coordinate import PlaneCoordinate
from my_class.Plane.Plane import Plane
from my_class.Plane.PlaneCommandRouter import PlaneCommandRouter
import time
HOST = "127.0.0.1"  # The server hostname or IP address
PORT = 65432  # The port used by the server

class PlaneClient():
    def __init__(self,start_coordinate:tuple=(0,200,200)):
        self.plane=Plane(0,start_coordinate)
        self.coordinate=PlaneCoordinate(start_coordinate)
        self.planecommmand=PlaneCommandRouter(self.plane)

        
    def start_clinet(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("Connected to the airport.")
            d_cordinate=(0,0,0)
            while True:

                    if self.difference(d_cordinate):
                        cord=self.plane.coordinate.send_json()
                        s.sendall(str(cord).encode('utf-8'))
                        d_cordinate=self.plane.coordinate.coordinates()
                        print(self.plane.coordinate)

                    if s.recv(2024):
                        data= s.recv(2024)
                        self.planecommmand.command(data) #handle movement
                        time.sleep(1)



    def difference(self,last_cooridane:tuple,dif=9):
        """ when difference is more than 'd' then retrun True"""
        actuall=self.coordinate.coordinates()
        dif_tuple = (abs(actuall[0] - last_cooridane[0]), abs(actuall[1] - last_cooridane[1]), abs(actuall[2] - last_cooridane[2]))

        if any(d > dif for d in dif_tuple):
            return True

                

if __name__=="__main__":
    client=PlaneClient()
    client.start_clinet()
