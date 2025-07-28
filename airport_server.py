import socket
import json
from datetime import datetime
from my_class.ServerConnection import ServerConnetions

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
VERSION = "0.0.1"
CREATION_DATE = datetime.now()
MAX_PLANES=100
class Server:
    def __init__(self):
        self.response=None    
        self.servcon=ServerConnetions(MAX_PLANES)
        self.number_of_planes=0
    #    self.connetions=[] #list of connetions       

    def start_server(self):
                
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.bind((HOST, PORT))
                s.listen()
                print(f"Airport Server started at {HOST}:{PORT}")
                temp=0
                while True:
                    n_conn, n_addr = s.accept()
                    self.servcon.get_new_connetion(n_conn,n_addr)


                    self.number_of_planes=self.servcon.active_planesconnection()
                    if self.number_of_planes != temp:
                         print(f"Liczba samolotow {self.number_of_planes}")
                         self.number_of_planes = temp
                         

                    
if __name__ == "__main__":
    server=Server()
    server.start_server()
