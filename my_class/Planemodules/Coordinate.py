
import json,math
import numpy as np


class Coordinate():
    def __init__(self,coordinate:tuple=(0,0,0)):
        """crnds: actual coordinates"""
        self.width=coordinate[0]
        self.length=coordinate[1]
        self.height=coordinate[2]

    def __str__(self):
        return f"x:{self.width}, y:{self.length}, z:{self.height}"
    
    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return self.coordinates() == other.coordinates()
        if isinstance(other, tuple):
            return self.coordinates() == other
        return NotImplemented
    
    def coordinates(self)->tuple:
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
    
    def get_numpy_coordinate(self):
        return np.array([self.width,self.length,self.height])

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

    def distance_to(self, other: "Coordinate") -> float:
        """Count distance to the other object"""
        return math.sqrt(
            (self.width - other.width) ** 2 +
            (self.length - other.length) ** 2 +
            (self.height - other.height) ** 2
        )

