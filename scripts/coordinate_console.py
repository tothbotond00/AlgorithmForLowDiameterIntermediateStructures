from enum import Enum

# Basic Coordinate aritrmetrics in the hexagon plane
class Coordiante:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def add(self,c2):
        self.x = self.x + c2.getX()
        self.y = self.y + c2.getY()
    def mix(self,c2):
        return Coordiante(self.x + c2.getX(), self.y + c2.getY())

# Direction for Even numbered columns
class DirectionEven(Enum):
    N = Coordiante(0,-1)
    S = Coordiante(0,1)
    NE = Coordiante(1,-1)
    SE = Coordiante(1,0)
    NW = Coordiante(-1,-1)
    SW = Coordiante(-1,0)

# Dirction for Odd numbered columns
class DirectionOdd(Enum):
    N = Coordiante(0,-1)
    S = Coordiante(0,1)
    NE = Coordiante(1,0)
    SE = Coordiante(1,1)
    NW = Coordiante(-1,0)
    SW = Coordiante(-1,1)