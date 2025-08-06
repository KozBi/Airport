import socket
#from concurrent.futures import ThreadPoolExecutor
from my_class.Plane.Plane import Plane
import threading
import json
import logging
import random
from my_class.Plane.Plane import Plane


class PlaneConnetion:
    def __init__(self,conn:socket, addr,server_ref,plane: Plane):
        self.conn:socket=conn
        self.addr=addr
        self.server_ref=server_ref     
        self.plane = plane
        self.connection_id = self.plane.id
        self.plane.connection=self #  Plane.connection jest ustawiane w konstruktorze PlaneConnection, więc nie musisz robić tego wcześniej w Server
        self.planecomunicationjson=PlaneComuncationJson(self.plane)

        self.connection = threading.Thread(target=self.handle_connetion,daemon=True)
        self.connection.start()

    def handle_connetion(self):
        with self.conn:
            print(f"New connection established, Connected by {self.addr} and {self.conn}")

            # 1 Receive initial position 
            data = self.conn.recv(2024)
            message =  json.loads(data.decode('utf-8')) # receive from client a task
            self.planecomunicationjson.handle_message(message)
            print(f"New Plane {self.plane.id}{self.plane.coordinate}")

            # 1 Send target
            cord={"target_coordinate": [100,100,1000]}
            cord=json.dumps(cord)
            self.conn.sendall(cord.encode('utf-8'))
            x = random.randint(100, 1000)

            while True:

                # 1 Receive position 
                data = self.conn.recv(2024)
                try:
                    message = json.loads(data.decode('utf-8')) # receive from client a task
                    self.planecomunicationjson.handle_message(message)
                    print(f"{self.plane.id}{self.plane.coordinate} Target x:{x}")

                    # 1 Send target
                    
                    cord={"target_coordinate": [x,100,1000]}
                    cord=json.dumps(cord)
                    self.conn.sendall(cord.encode('utf-8'))
                except: logging.DEBUG("No message from Plane client")
                if message == "stop":
                    print("Shutting down connection by user")
                    break           
            self.server_ref.remove_connection(self)


class ServerConnetions:
    def __init__(self,Max_planes=100):
        """Handle connections to planes"""
        self.connetions=[] #list of connetions
        self.Max_planes=Max_planes

        self.lock = threading.Lock()
        
    def active_planesconnection(self):
        """Return number of aktiv connections"""
        return len(self.connetions)

    def get_new_connection(self,conn:socket,addr,plane: Plane):
        if self.active_planesconnection() < self.Max_planes:
            with self.lock:
                new_con=PlaneConnetion(conn,addr,self,plane)
                self.connetions.append(new_con)
                return new_con
                
        else: pass # No place for the plane to do

    def remove_connection(self, planeconnection:PlaneConnetion):
        with self.lock:
            if planeconnection in self.connetions:
                print(f"Connection to plane {planeconnection.addr} has been deleted from Pool")
                self.connetions.remove(planeconnection)

class PlaneComuncationJson():
    def __init__(self,plane: Plane):
        self.plane=plane

    def handle_message(self,msg:dict):

        if isinstance(msg, dict):
            if msg["type"]=="position_update":
                new_position=msg["position"]
                self.plane.coordinate.set(new_position)
        else: logging.CRITICAL("Command is not a dict. Programing Error")
       

            
