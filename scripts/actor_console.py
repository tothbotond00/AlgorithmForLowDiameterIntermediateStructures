import coordinate_console as coordinate

class Actor:
    # Current position
    position = coordinate.Coordiante(0,0)
    
    # Does the actor carry a tile?
    hasTile = True
    
    def __init__(self, x, y):
        self.position = coordinate.Coordiante(x,y)

    step_counter = 0

    # Move in Direction (use Direction from direction.py)
    def move(self,direction, step_counter):
        self.position.add(direction)
        step_counter[0] += 1
        if self.hasTile:
            step_counter[1] += 1
        
    def getPosition(self):
        return self.position