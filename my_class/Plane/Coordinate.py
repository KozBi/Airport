import logging

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
        return {"x":self.width, "y":self.length, "z":self.height}



class PlaneCoordinate(Coordinate):
    def __init__(self,coordinate:tuple):
        super().__init__(coordinate)
        pass

    def update(self,coordintate:tuple):
        self.width += coordintate[0]
        self.length += coordintate[1]
        self.height += coordintate[2]


    def set(self,coordintate:tuple):
        self.width = coordintate[0]
        self.length = coordintate[1]
        self.height = coordintate[2]
