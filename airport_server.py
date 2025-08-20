import socket
import threading
from datetime import datetime
import logging
import time

from my_class.ServerConnection import ServerConnetions
from my_class.Airport.Airport import Airport
from my_class.Airport.Airportmodule import AirportLandRunway

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
VERSION = "0.0.1"
CREATION_DATE = datetime.now()
MAX_PLANES=100
RUNWAYS=[AirportLandRunway(2500,6000),AirportLandRunway(6000,5000)]

logging.basicConfig(level=logging.DEBUG)
# Clear logs only from matplotlib
logging.getLogger('matplotlib').setLevel(logging.WARNING)

class Server:
    def __init__(self):

        self.runways=RUNWAYS
        self.airport=Airport(self.runways) #whole logic
        self.servcon=ServerConnetions(self.airport,MAX_PLANES) # handle connections to planes
   #     self.response=None
        self.connection_checker = threading.Thread(target=self.check_connetions,daemon=True)
        self.connection_checker.start()


    def start_server(self):

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            logging.info(f"Airport Server started at {HOST}:{PORT}")

            while True:
                n_conn, n_addr = s.accept()
                self.get_new_plane_connetion(n_conn,n_addr)
                


    def get_new_plane_connetion(self,n_conn,n_addr):
        # 1 check if poolconnetion is not full
        if self.servcon.connection_possbile():
            #2 get a plane nummber (Inster new plane in DB and get a planne number)
            plane=self.airport.get_new_plane()   
            if plane:
                # 3 estahblish a new connetion in a new threat
                self.servcon.get_new_connection(n_conn,n_addr,plane) 
            else:
                logging.debug("Plane cannot be added to Database")
        else: logging.info("Maximal number of clients reached, plane cannot land")

    def check_connetions(self):
        while True:
            time.sleep(5)  # check every 5 second
            self.servcon.remove_connection()

    def start_airport(self):
        self.airport.start()
          
if __name__ == "__main__":

    server=Server()

    # def test():
    #     while True:
    #         print(server.servcon.active_planesconnection())
    #         time.sleep(1)

    threading.Thread(target=server.start_server, daemon=True).start() #connetion in a different threat
    #threading.Thread(target=test, daemon=True).start()
    server.start_airport()  # GUI must be called in main thread
    



    

    
