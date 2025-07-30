from PlaneCoordinate import PlaneCoordinate

class Plane():
    def __init__(self,id,coordinate:tuple):
        self.id=id
        self.planecoordinate=PlaneCoordinate(coordinate)
        self.landing=False
