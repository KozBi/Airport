
class Area():
    """Base class"""
    def __init__(self,width,length, height):
        self.width=width
        self.length=length
        self.height=height


class AirportArea(Area):
    def __init__(self,width=10000,length=10000, height=5000):
        super().__init__(width,length,height)


class RunwayArea(Area):
    def __init__(self,width,length):
        height=0
        super().__init__(width,length,height)