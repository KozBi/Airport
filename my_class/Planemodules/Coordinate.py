import logging
import json

class Coordinate():
    def __init__(self,coordinate:tuple=(0,0,0)):
        """crnds: actual coordinates"""
        self.width=coordinate[0]
        self.length=coordinate[1]
        self.height=coordinate[2]

    def __str__(self):
        return f"x:{self.width}, y:{self.length}, z:{self.height}"
    
    def coordinates(self):
        "Return tuple (width,lenght,height)"
        return (self.width,self.length,self.height)

    def send_json(self):
        sendjson={
                "type": "position_update",
                "position": [self.width, self.length, self.height]
                }
        return (json.dumps(sendjson).encode('utf-8'))
    
    def get_list_coordinates(self):
        return [self.width,self.length,self.height]

class PlaneCoordinate(Coordinate):

    def __init__(self,coordinate:tuple=(0,0,0)):
        """     (x,y,z)
            x - widht
            y - lenght
            z - hieght
        """
        super().__init__(coordinate)
        pass

    def update(self,coordintate:tuple):
        """move object with (x,y,z)"""
        self.width += coordintate[0]
        self.length += coordintate[1]
        self.height += coordintate[2]


    def set(self,coordintate:tuple):
        """set new position (x,y,z)"""
        self.width = coordintate[0]
        self.length = coordintate[1]
        self.height = coordintate[2]
