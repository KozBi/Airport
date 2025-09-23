import socket
import json
from my_class.Planemodules.Coordinate import PlaneCoordinate
from my_class.Planemodules.Planemodule import PlaneClinet
from my_class.Planemodules.PlaneCommandRouter import PlaneCommandRouter
import time
import logging
import random,threading
HOST = "127.0.0.1"  # The server hostname or IP address
PORT = 65432  # The port used by the server

NUMBER_OF_PLANES=1

start_coordinate=None
BORDER_COORDINATE=(2000, 5000)

class Client():

    
    def __init__(self,start_coordinate:tuple=(0,0,0)):
        self.plane=PlaneClinet(0,start_coordinate)
        self.planecommmand=PlaneCommandRouter(self.plane)

        
    def start_clinet(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("Connected to the airport.")

            # 1. Send initial position
            position = self.planecommmand.answer()
            s.sendall(position)

            # 2. Receive target
            data = s.recv(2048)
            command=json.loads(data.decode('utf-8')) 

            while True:               
                try:
                    # 3. Simulate move or reject connection
                    self.planecommmand.handle_command(command) # movement
                    time.sleep(1)
                    if NUMBER_OF_PLANES ==1:
                        print(f"ACTUAL COORDINATE{self.plane.coordinate.coordinates()}")
                        print(F"TARGET {self.planecommmand._target_coordinate.coordinates()}")

                    # 4. Send answer
                    answer=self.planecommmand.answer()
                    s.sendall(answer)

                    # 5. Fuel check
                    if self.plane.fuel_check():
                        # to do - log in database - crash
                        self.planecommmand.dissconect=True

                    # 5. Check for command
                    s.settimeout(0.5)
                    
                    new_data = s.recv(2048)
                    if new_data:
                        command  = json.loads(new_data.decode('utf-8')) 
                        self.planecommmand.handle_command(command)
                    # If plane already land, shut down the connection

                    if self.planecommmand.dissconect:
                        print("Plane hit the target, dissconnection")
                        break
                # connection lost
                except Exception as e:
                        logging.info("No data from Server")
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
    for i in range(NUMBER_OF_PLANES):
        client = Client(generate_border_coordinate())
        t = threading.Thread(target=client.start_clinet, daemon=True)
        threads.append(t)
        t.start()
        time.sleep(0.2) 

    for t in threads:
        t.join()


