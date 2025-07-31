from my_class.Airport.Plane.Coordinate import PlaneCoordinate

class Plane():
    def __init__(self,id,coordinate:tuple):
        self.id=id
        self.coordinate=PlaneCoordinate(coordinate)
        self.landing=False
        self.connection=None



