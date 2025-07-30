from my_class.DataBase.DataBaseConnection import DataBaseConnection
import psycopg2
from psycopg2.errors import UniqueViolation


class DataBaseLog():
    def __init__(self, databaseconnection:DataBaseConnection):
        self.databaseconnection=databaseconnection
    
    def connection_established(self):
        try:
            with self.databaseconnection.get_cursor() as curr:
                curr.execute("INSERT INTO Planes DEFAULT VALUES RETURNING id")
                plane_id = curr.fetchone()[0]
                return (plane_id)
        except psycopg2.Error as e:
                print("Database error:", e)
                return None


    
