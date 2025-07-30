import socket
import json
from datetime import datetime
import logging

from my_class.ServerConnection import ServerConnetions
from my_class.DataBase.DataBaseConnection import DataBaseConnection
from my_class.DataBase.DataBaseLog import DataBaseLog
from my_class.Airport import Airport
from my_class.Plane import Plane

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
VERSION = "0.0.1"
CREATION_DATE = datetime.now()
MAX_PLANES=100
logging.basicConfig(level=logging.DEBUG)

class Server:
    def __init__(self):

        self.servcon=ServerConnetions(MAX_PLANES)
        self.databaseconnection=DataBaseConnection()
        self.databaselog=DataBaseLog(self.databaseconnection)
        self.airport=Airport()

        self.response=None
        # self.number_of_planes=0

    def start_server(self):

            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((HOST, PORT))
                s.listen()
                logging.info(f"Airport Server started at {HOST}:{PORT}")
                temp=0
                while True:
                    n_conn, n_addr = s.accept()
                    self.get_new_plane_connetion(n_conn,n_addr)

                    # self.number_of_planes=self.servcon.active_planesconnection()
                    # if self.number_of_planes != temp:
                    #      print(f"Number of planes{self.number_of_planes}")
                    #      self.number_of_planes = temp


    def get_new_plane_connetion(self,n_conn,n_addr):
        new_connection=self.servcon.get_new_connection(n_conn,n_addr)
        plane_id=self.databaselog.connection_established()
        if plane_id is not None:
            self.airport.new_plane(Plane(plane_id))
            new_connection.connection_id=plane_id
        else:
            logging.debug("Plane cannot be added to Database")


if __name__ == "__main__":
    server=Server()
    server.start_server()
