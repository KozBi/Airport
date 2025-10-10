from fastapi import FastAPI, HTTPException
from my_class.Airport.Airportmodule import AirPortPlanes
from my_class.DataBase.DataBaseLog import AirportLogbook


class AirPortRestAPI:
    def __init__(self,airportplanes:AirPortPlanes,databse:AirportLogbook):
        self.airportplanes=airportplanes
        self.database=databse
        self.app=FastAPI(title="Airport REST API")

        #endpoints
        self.app.get("/planes_number")(self.get_planes_number)
        self.app.get("/planes")(self.get_planes)

    def get_planes_number(self):
        return {"planes_number": len(self.airportplanes.planes)}
    
    def get_planes(self):
        return {"planes": str(self.airportplanes.planes)}


def start_api(airportplanes:AirPortPlanes,databse:AirportLogbook):
    api = AirPortRestAPI(airportplanes,databse)
    return api.app

# @app.post("/items")
# def create_item(item:str):
#     items.append(item)
#     return items

# @app.get("/items/{item_id}")
# def get_item(item_id:int) -> str:
#     if item_id<len(items):        
#         item=items[item_id]
#         return item
#     else:
#         raise HTTPException(status_code=404, detail="Item not found")