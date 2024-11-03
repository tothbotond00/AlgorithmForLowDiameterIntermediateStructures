import coordinate
import matplotlib.pyplot as plt

class Actor:
    # Current position
    position = coordinate.Coordiante(0,0)
    
    # Does the actor carry a tile?
    hasTile = True
    
    def __init__(self, x, y, time):
        self.position = coordinate.Coordiante(x,y)
        self.time = time
        

    def changeTime(self, time):
        if round(self.time + time, 1) > 0:
            self.time = round(self.time+time, 1)
            print("Time: " + str(self.time))
        elif round(self.time + time, 1) == 0:
            self.time = 0.01
            print("Time: " + str(self.time))

    # Move in Direction (use Direction from direction.py)
    def move(self,direction, drawer, ax, plane):
        self.position.add(direction)
        drawer.draw_hex_grid(ax, plane)
        plt.draw()
        plt.pause(self.time)
        
    def getPosition(self):
        return self.position