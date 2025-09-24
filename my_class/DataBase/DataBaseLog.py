import psycopg2
from contextlib import contextmanager
import json

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
    def __init__(self,planes:AirPortPlanes):
        self.planes:AirPortPlanes=planes

    
    def check_collision(self):
        print("Sprawdzam kolizje cały czas: :)")
        pass


class AirportLogbook():
    def __init__(self,ref_planes:AirPortPlanes, host='localhost', database='airport', user='postgres', password='admin'):
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
        
    def check_collision(self):
         self.airportlogcollision.check_collision()
         
        



    
