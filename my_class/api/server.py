from fastapi import FastAPI, HTTPException
from my_class.Airport.Airportmodule import AirPortPlanes


class AirPortRestAPI:
    def __init__(self,airportplanes:AirPortPlanes):
        self.airportplanes=airportplanes
        self.app=FastAPI(title="Airport REST API")

        #endpoints
        self.app.get("/planes_number")(self.get_planes_number)

    def get_planes_number(self):
        return {"planes_number": len(self.airportplanes.planes)}


def start_api(airportplanes:AirPortPlanes):
    api = AirPortRestAPI(airportplanes)
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