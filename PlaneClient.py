import socket
import json

HOST = "127.0.0.1"  # The server hostname or IP address
PORT = 65432  # The port used by the server

class PlaneClient():
    def __init__(self):
        pass

    def start_clinet(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            print("Connected to the airport.")
            while True:
                command=input(">>>").strip()
                s.sendall(command.encode('utf-8'))
                data = s.recv(2024)
                response = json.loads(data.decode('utf-8'))
                print(response)
                

if __name__=="__main__":
    client=PlaneClient()
    client.start_clinet()
