import psycopg2
from contextlib import contextmanager
import json
from itertools import combinations
import logging

from my_class.Planemodules.Planemodule import PlaneAirport
from my_class.Airport.Airportmodule import AirPortPlanes

class DataBaseConnection():
    def __init__(self, host='localhost', database='airport', user='postgres', password='admin'):
        """establish connection to database"""
        self.host = host
        self.database = database
        self.user = user
        self.password = password     
        self._ensure_tables()

    @contextmanager #to work with with
    def get_cursor(self): 
        conn = psycopg2.connect( #establish connection
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password)
        try:
            curr = conn.cursor() #set cursor
            yield curr #give curr as a output
            conn.commit() 
        except Exception as e:
            conn.rollback()
            raise e
        finally: #after with code close connection.
            curr.close()
            conn.close()  


    def _ensure_tables(self):
        with self.get_cursor() as curr:
            curr.execute("""
                CREATE TABLE IF NOT EXISTS Planes (
                    id BIGSERIAL PRIMARY KEY,
                    connection_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    has_landed Bool NOT NULL DEFAULT FALSE,
                    start_coordinate JSONB DEFAULT '{}' NOT NULL
                );
            """)

            curr.execute("""
                CREATE TABLE IF NOT EXISTS Collision (
                    id BIGSERIAL PRIMARY KEY,
                    Plane INTEGER REFERENCES Planes(id),
                    reason VARCHAR(50),
                    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
            """)

class AirportLogCollision():
    def __init__(self,planes):
        self.planes=planes

    
    def check_collision(self):
        """return list of crashed planes:
        crashed plane id,
        reson,
        the plane he collided with
        """
        crashed_planes=[]
        for plane in self.planes:
            if plane.empy_tank:
                crashed_planes.append((plane.id,"No fuel"))

        if len(self.planes)>=2:
            for plane, nextplane in combinations(self.planes,2):
                plane:PlaneAirport
                nextplane:PlaneAirport
                distance=plane.coordinate.distance_to(nextplane.coordinate)
                if distance <=20:
                    crashed_planes.append((plane.id,"collision between planes",nextplane.id))

        return crashed_planes
         

class AirportLogbook():
    def __init__(self,ref_planes, host='localhost', database='airport', user='postgres', password='admin'):
        self.host=host
        self.database=database
        self.user=user
        self.password=password
        self.databaseconnection=DataBaseConnection(host=self.host, database=self.database, user=self.user, password=self.password)
        self.airportlogcollision=AirportLogCollision(ref_planes)

    def insert_new_connetion(self):
        """ Try to write connetion in DB, 
        if succesfull return plane id"""
        try:
            with self.databaseconnection.get_cursor() as curr:
                curr.execute("INSERT INTO Planes DEFAULT VALUES RETURNING id")
                plane_id = curr.fetchone()[0]
                return (plane_id)
        except psycopg2.Error as e:
                print("Database error:", e)
                return None
        
    def update_start_coordinate(self,plane:PlaneAirport)-> None:
        """Update start coordinate for plaene"""
        plane_id=plane.id
        coordinate=json.dumps(plane.coordinate.coordinates())
        try:
            with self.databaseconnection.get_cursor() as curr:
                curr.execute("UPDATE Planes SET start_coordinate=%s WHERE ID=%s;", (coordinate,plane_id))
        except psycopg2.Error as e:
                print("Database error:", e)
                return None
        
    def update_landing_info(self,plane:PlaneAirport)-> None:
        """Update landing information"""
        plane_id=plane.id
        try:
            with self.databaseconnection.get_cursor() as curr:
                curr.execute("UPDATE Planes SET has_landed=%s WHERE ID=%s;", (True,plane_id))
        except psycopg2.Error as e:
                print("Database error:", e)
                return None
        
    def log_collision(self):
        crahsed_planes=self.airportlogcollision.check_collision()

        for values in crahsed_planes:
            try:
                with self.databaseconnection.get_cursor() as curr:
                    print(values[0],values[1])
                    curr.execute("Insert INTO Collision (Plane ,reason) VALUES(%s,%s);", (values[0],values[1]))
                    logging.warning("Collision has been occured")
            except psycopg2.Error as e:
                    print("Database error:", e)
                    return None
        



    
