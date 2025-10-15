from fastapi import FastAPI, HTTPException
from my_class.Airport.Airportmodule import AirPortPlanes
from my_class.DataBase.DataBaseLog import AirportLogbook
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from sqlalchemy import create_engine, Column, Integer, Boolean, DateTime , text , JSON
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

#  Database used PSQL
DATABASE_URL = "postgresql+psycopg2://postgres:admin@localhost/airport"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# Plane Model
class PlaneLog(Base):
    __tablename__ = "planes" 

    id = Column(Integer, primary_key=True, index=True)
    connection_time = Column(
        DateTime,
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP")
    )
    has_landed = Column(Boolean, nullable=False, server_default=text("FALSE"))
    start_coordinate = Column(JSON, nullable=False, server_default=text("'{}'::jsonb"))



class AirPortRestAPI:
    def __init__(self,airportplanes:AirPortPlanes,databse:AirportLogbook):
        self.airportplanes=airportplanes
        self.database=databse
        self.app=FastAPI(title="Airport REST API")

        #endpoints
        self.app.get("/planes_number")(self.get_planes_number)
        self.app.get("/planes")(self.get_planes)
        self.app.get("/plane/{id}")(self.get_plane)
        self.app.get("/plane_db/{id}")(self.get_plane_info)


    def get_planes_number(self):
        return {"planes_number": len(self.airportplanes.planes)}
    
    def get_planes(self):
        return {"planes": str(self.airportplanes.planes)}
    
    def get_plane(self,id):
        if self.airportplanes.planes.get(int(id)):
            return str(self.airportplanes.planes.get(int(id)))
        else:
            raise HTTPException(status_code=404, detail=f"Item {id} not found")
        
    def get_plane_info(self,id):
        
        with Session(engine) as session:
            result = session.query(PlaneLog).filter(PlaneLog.id==int(id)).first()
            if result:
                print(result)
                return {
                    "id": result.id,
                    "connection_time": result.connection_time,
                    "has_landed": result.has_landed,
                    "start_coordinate": result.start_coordinate
                }
               # print (result)
               # return result
            else:
                raise HTTPException(status_code=404, detail=f"Plane with id {id} not found")



def start_api(airportplanes:AirPortPlanes,databse:AirportLogbook):
    api = AirPortRestAPI(airportplanes,databse)
    return api.app






