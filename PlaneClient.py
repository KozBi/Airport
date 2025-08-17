import socket
import json
from my_class.Planemodules.Coordinate import PlaneCoordinate
from my_class.Planemodules.Planemodule import Plane
from my_class.Planemodules.PlaneCommandRouter import PlaneCommandRouter
import time
import logging
import random,threading
HOST = "127.0.0.1"  # The server hostname or IP address
PORT = 65432  # The port used by the server


start_coordinate=None
BORDER_COORDINATE=(2000, 5000)

class PlaneClient():

    
    def __init__(self,start_coordinate:tuple=(0,0,0)):
        self.plane=Plane(0,start_coordinate)
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
                   # print(f"Aktual coordinate{self.plane.coordinate}")
                    #print(f"Target coordinate {self.planecommmand._target_coordinate.coordinates()}")

                    # 5. Check for command
                    s.settimeout(0.5)
                    try:
                        new_data = s.recv(2048)
                        if new_data:
                            command  = json.loads(new_data.decode('utf-8')) 
                            self.planecommmand.command(command)
                    except socket.timeout:
                        logging.info("No data from Server")
                        continue
                    # If plane already land, shut down the connection
                    if self.planecommmand.dissconect:
                        print("Plane hit the target, dissconnection")
                        break
                

def generate_border_coordinate(max_coord=10000, altitude_range=BORDER_COORDINATE):
    # Generate x or y
    if random.choice([True, False]):  
        # if True then y is 0 or 10 000, x=random
        x = random.randint(0, max_coord)
        y = random.choice([0, max_coord])
    else: # if False then x is 0 or 10 000, y=random
        x = random.choice([0, max_coord])
        y = random.randint(0, max_coord)

    # * unpuck funnction tuple to 2 variables
    z = random.randint(*altitude_range)
    return (x, y, z)


if __name__ == "__main__":
    threads = []
    for i in range(3):
        client = PlaneClient(generate_border_coordinate())
        t = threading.Thread(target=client.start_clinet, daemon=True)
        threads.append(t)
        t.start()
        time.sleep(0.2) 

    for t in threads:
        t.join()
