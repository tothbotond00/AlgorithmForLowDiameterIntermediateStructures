import coordinate
class Actor:
    # Current position
    position = coordinate.Coordiante(0,0)
    
    # Does the actor carry a tile?
    hasTile = True
    
    def __init__(self, x, y):
        self.position = coordinate.Coordiante(x,y)
        
    # Move in Direction (use Direction from direction.py)
    def move(self,direction):
        self.position.add(direction)
        
    def getPosition(self):
        return self.position