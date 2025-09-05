import unittest, sys, os
import psycopg2

from my_class.Planemodules.Planemodule import PlaneAirport
from my_class.DataBase.DataBaseLog import AirportLogbook

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class TestDataBase(unittest.TestCase):

    #classmethod,  to run only once connection to temp database
    @classmethod
    def setUpClass(cls):
        cls.conn=psycopg2.connect(
                host='localhost',
                database='test_airport',       
                user='postgres',      
                password='admin')
        cls.curs=cls.conn.cursor()
        
    
    def setUp(self):   
        self.database=AirportLogbook(database="test_airport")
        self.dummyplanes=[PlaneAirport(1,(10000,2000,0)),
                    PlaneAirport(2,(1000,20000,0)),
                    PlaneAirport(3,(9000,3000,5000))
                    ,PlaneAirport(4,(8000,0000,0000))] #plane 4 is alredy in runway1
        self.dummyplanes0=self.dummyplanes[0]
        self.dummyplanes1=self.dummyplanes[1]
        self.dummyplanes2=self.dummyplanes[2]
        self.dummyplanes3=self.dummyplanes[3]
        self.reset_database()
         
    @classmethod
    def tearDownClass(cls):
        cls.conn.close()

    #reset test_mailbox each tim when test is called.
    def reset_database(self):
        self.curs.execute("TRUNCATE TABLE planes RESTART IDENTITY CASCADE;")
        for p in self.dummyplanes:
            p:PlaneAirport
            self.curs.execute("""
                            INSERT INTO planes (id, has_landed, start_coordinate)
                            VALUES (%s, DEFAULT, DEFAULT)
                            """,
                            (p.id,))
        self.conn.commit()

    def test_update_start_coordinate(self):
        self.database.update_start_coordinate(self.dummyplanes0)
        self.curs.execute("""SELECT start_coordinate FROM planes WHERE id=%s;""", (self.dummyplanes0.id,))
        result=self.curs.fetchone()
        # check if updated coordinates are correct
        self.assertEqual(self.dummyplanes0.coordinate.get_list_coordinates(),result[0])
                          
        
