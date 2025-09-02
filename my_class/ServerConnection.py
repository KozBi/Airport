import socket
#from concurrent.futures import ThreadPoolExecutor
from my_class.Planemodules.Planemodule import Plane
import threading
import json
import logging
import random
from my_class.Planemodules.Planemodule import PlaneAirport
from my_class.Airport.Airport import Airport
from my_class.Planemodules.Planemodule import PlaneCoordinate


class PlaneConnetion:
    def __init__(self,conn:socket, addr,server_ref,plane: PlaneAirport,reject_connetion=False):
        self.conn:socket=conn
        self.addr=addr
        self.server_ref=server_ref     
        self.plane = plane
        self.connection_id = self.plane.id
        self.plane.connection=self #  Plane.connection jest ustawiane w konstruktorze PlaneConnection, więc nie robię tego wcześniej w Server
        self.connetion_end = False
        self.reject_connection=reject_connetion
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

            # 2 Send target or reject coonnection 
            if self.reject_connection:
                self.connetion_end=True
                reject_message={"release": False}
                reject_message=json.dumps(reject_message)
                self.conn.sendall(reject_message.encode('utf-8'))
                logging.info("Client has been rejected")
            else:
                cord=self.plane.get_target()
                cord=json.dumps(cord)
                self.conn.sendall(cord.encode('utf-8'))

            while not self.reject_connection:
                try:
                # 1 Receive position 
                    data = self.conn.recv(2024)
                
                    message = json.loads(data.decode('utf-8')) # receive from client a task
                    self.planecomunicationjson.handle_message(message)

                    # 2 Send target
                    target=self.plane.target_coordinate.coordinates()
                    message={"target_coordinate": target}

                    # 2a If plane landed - release shut down the connection
                    if self.plane.landed():
                          message={"release_disc": True}  

                    message=json.dumps(message)
                    self.conn.sendall(message.encode('utf-8')) 
                
                    # if client close the connetion it must be removed form pool as well
                    if self.planecomunicationjson.shut_down:
                        self.connetion_end=True
                        return False  
                    
                except ConnectionResetError:
                    logging.info("Client connettion shut down, plane removed")
                    self.connetion_end = True
                    return False
                except Exception as e:
                    self.connetion_end = True
                    return False    



class ServerConnetions:
    """Class resposbile to handle all connetions,
    add a new one or remove exsisting one."""
    def __init__(self,airport_ref:Airport,Max_planes=100,):
        """Handle connections to planes"""
        self.connetions=[] #list of connetions
        self.Max_planes=Max_planes
        self.airport_ref=airport_ref

        self.lock = threading.Lock()

    def connection_possbile(self):
        return len(self.connetions)<self.Max_planes
        
    def active_planesconnection(self):
        """Return number of aktiv connections"""
        return len(self.connetions)

    def get_new_connection(self,conn:socket,addr,plane: Plane):
        """ estahblish a new connetion in a new threat or reject when max number of clients is reached"""
        with self.lock:
            if self.connection_possbile():       
                new_con=PlaneConnetion(conn,addr,self,plane)                          
            else: 
                new_con=PlaneConnetion(conn,addr,self,plane,reject_connetion=True) 
                logging.info("Plane cannot be added - Max numebers of clients")
            self.connetions.append(new_con)
            return new_con
    def remove_connection(self):
            for planeconnetion in self.connetions[:]: #[:] # iterate over a copy to safely modify the original list!
                if planeconnetion.connetion_end:
                    with self.lock:
                        self.connetions.remove(planeconnetion) #remove connetion form the list
                        self.airport_ref.airportplanes.remove_plane(planeconnetion.plane) #remove connetions from the Airport class
                        logging.info(f"Connection to plane {planeconnetion.addr} has been deleted from Pool")


class PlaneComuncationJson():
    def __init__(self,plane: Plane):
        self.plane=plane

    def handle_message(self,msg:dict):
        self.shut_down=False

        if isinstance(msg, dict):
            if msg["type"]=="position_update":
                new_position=msg["position"]
                self.plane.coordinate.set(new_position)
                self.plane.fuel=msg["fuel"]

            if msg["type"]=="colission":
                self.shut_down=True
                logging.info(f'Colission - reason: {msg["reason"]}')

        else: logging.CRITICAL("Command is not a dict. Programing Error")
       

            
