import socket
import json
from my_class.Airport.Plane.Coordinate import PlaneCoordinate
import time
HOST = "127.0.0.1"  # The server hostname or IP address
PORT = 65432  # The port used by the server

class PlaneClient():
    def __init__(self):
        self.coordinate=PlaneCoordinate((10000,1000,5432))
        
    def start_clinet(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("Connected to the airport.")
            t_cordinate=(0,0,0)
            while True:

                self.coordinate.move(-10,0,0)
                time.sleep(1)
                if self.difference(t_cordinate):
                    cord=self.coordinate.send_json()
                    s.sendall(str(cord).encode('utf-8'))
                    t_cordinate=self.coordinate.coordinates()
                    print(self.coordinate)

       #         data = s.recv(2024)
        #        response = json.loads(data.decode('utf-8'))


    def difference(self,last_cooridane:tuple,dif=9):
        """ when difference is more than 'd' then retrun True"""
        actuall=self.coordinate.coordinates()
        dif_tuple = (abs(actuall[0] - last_cooridane[0]), abs(actuall[1] - last_cooridane[1]), abs(actuall[2] - last_cooridane[2]))

        if any(d > dif for d in dif_tuple):
            return True

                

if __name__=="__main__":
    client=PlaneClient()
    client.start_clinet()
