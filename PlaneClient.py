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

            # 1. Send initial position
            position = self.plane.coordinate.send_json()
            s.sendall(position)

            # 2. Receive target
            data = s.recv(2048)
            command=json.loads(data.decode('utf-8')) 

            while True:               
                    
                    # 3. Simulate move
                    self.planecommmand.command(command) # movement
                    time.sleep(1)

                    # 4. Send current position
                    cord=self.plane.coordinate.send_json()
                    s.sendall(cord)
                    print(self.plane.coordinate)

                    # 5. Check for command
                    s.settimeout(0.5)
                    try:
                        new_data = s.recv(2048)
                        if new_data:
                            command  = json.loads(new_data.decode('utf-8')) 
                            self.planecommmand.command(command)
                    except socket.timeout:
                        print("Czekam")
                        continue
                

if __name__=="__main__":
    client=PlaneClient()
    client.start_clinet()
