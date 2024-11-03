import coordinate
import matplotlib.pyplot as plt

class Actor:
    # Current position
    position = coordinate.Coordiante(0,0)
    
    # Does the actor carry a tile?
    hasTile = True
    
    def __init__(self, x, y):
        self.position = coordinate.Coordiante(x,y)
        
    # Move in Direction (use Direction from direction.py)
    def move(self,direction, drawer, ax, plane):
        self.position.add(direction)
        drawer.draw_hex_grid(ax, plane)
        plt.draw()
        plt.pause(0.1)
        
    def getPosition(self):
        return self.position