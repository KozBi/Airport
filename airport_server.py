import socket
import json
from datetime import datetime
import logging

from my_class.ServerConnection import ServerConnetions

from my_class.Airport.Airport import Airport
from my_class.Airport.Plane.Plane import Plane

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
VERSION = "0.0.1"
CREATION_DATE = datetime.now()
MAX_PLANES=100
logging.basicConfig(level=logging.DEBUG)

class Server:
    def __init__(self):

        self.servcon=ServerConnetions(MAX_PLANES) # handle connections to planes
        self.airport=Airport() #whole logic
        self.response=None

    def start_server(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            logging.info(f"Airport Server started at {HOST}:{PORT}")
            while True:
                n_conn, n_addr = s.accept()
                self.get_new_plane_connetion(n_conn,n_addr)


    def get_new_plane_connetion(self,n_conn,n_addr):
        plane=self.airport.get_new_plane()     
        if plane:
            self.servcon.get_new_connection(n_conn,n_addr,plane) #create a connetion to the plane
        else:
            logging.debug("Plane cannot be added to Database")


if __name__ == "__main__":
    server=Server()
    server.start_server()
