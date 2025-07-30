
class Coordinate():
    def __init__(self,coordinate:tuple):
        self.coordinate=coordinate
        self.width=coordinate[0]
        self.length=coordinate[1]
        self.height=coordinate[2]


class PlaneCoordinate(Coordinate):
    def __init__(self):
        pass
    
    def move(self,w=0,l=0,h=0):
        self.width=+w
        self.length=+l
        self.height=+h