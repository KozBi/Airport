import psycopg2
from contextlib import contextmanager



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
                    has_landed Bool NOT NULL DEFAULT FALSE
                );
            """)

            curr.execute("""
                CREATE TABLE IF NOT EXISTS Colision (
                    id BIGSERIAL PRIMARY KEY,
                    Plane1 INTEGER REFERENCES Planes(id),
                    Plane2 INTEGER REFERENCES Planes(id),
                    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
                );
            """)


class AirportLogbook():
    def __init__(self, host='localhost', database='airport', user='postgres', password='admin'):
        self.host=host
        self.database=database
        self.user=user
        self.password=password
        self.databaseconnection=DataBaseConnection(host=self.host, database=self.database, user=self.user, password=self.password)
    
    def connection_established(self):
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


    
