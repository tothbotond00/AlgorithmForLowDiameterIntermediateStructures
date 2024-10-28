import actor
import coordinate
import random

class Plane:
    actor = actor.Actor(0,0)
    tiles = []
    x = 0
    y = 0
    
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        for i in range(x):
            helper = []
            for j in range(y):
                helper.append(False)
            self.tiles.append(helper)
            
        # Open the file in read mode
        with open(f'./data/{filename}', 'r') as file:
        # Iterate through each line in the file
            i = 0
            for line in file:
                for j in range(len(line)):
                    #If 1 then it is a simple Tile
                    if line[j] != '\n' and int(line[j]) == 1:
                        self.tiles[j][i] = True
                    #If two then it is a simple tile with the actor
                    if line[j] != '\n' and int(line[j]) == 2:
                        self.tiles[j][i] = True
                        self.actor = actor.Actor(j,i)
                i += 1
        
    def getTile(self, x, y):
        return self.tiles[x][y]

    def getActor(self):
        return self.actor
    
    # Moves the Actor to the proper coordinate based on a random direction (For testing purpose only)
    def moveActor(self):
        if(self.actor.getPosition().getX() % 2 == 0):
            direction = random.choice(list(coordinate.DirectionEven))
        else :
            direction = random.choice(list(coordinate.DirectionOdd))
        actorPosition = self.actor.getPosition()
        newposition = actorPosition.mix(direction.value)
        if self.tiles[newposition.getX()][newposition.getY()] == True:
            self.actor.move(direction.value)