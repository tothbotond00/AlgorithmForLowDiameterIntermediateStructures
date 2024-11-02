import time
import actor
import coordinate
import matplotlib.pyplot as plt
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
    def moveActor(self, ax, drawer):
        # if(self.actor.getPosition().getX() % 2 == 0):
        #     direction = random.choice(list(coordinate.DirectionEven))
        # else :
        #     direction = random.choice(list(coordinate.DirectionOdd))
        # actorPosition = self.actor.getPosition()
        # newposition = actorPosition.mix(direction.value)
        # if self.tiles[newposition.getX()][newposition.getY()] == True:
        #     self.actor.move(direction.value)

        while True:
        
            if(self.actor.getPosition().getX() % 2 == 0):
                directionFirst = coordinate.DirectionEven.NW
                directionSecond = coordinate.DirectionEven.SW
                directionThird = coordinate.DirectionEven.N
            else:
                directionFirst = coordinate.DirectionOdd.NW
                directionSecond = coordinate.DirectionOdd.SW
                directionThird = coordinate.DirectionOdd.N

            actorPosition = self.actor.getPosition()
            newPositionFirst = actorPosition.mix(directionFirst.value)
            newPositionSecond = actorPosition.mix(directionSecond.value)
            newPositionThird = actorPosition.mix(directionThird.value)
            drawer.draw_hex_grid(ax, self)
            plt.draw()
            plt.pause(1)
            if(self.getTile(newPositionFirst.getX(),newPositionFirst.getY()) == True):
                self.actor.move(directionFirst.value)
            elif (self.getTile(newPositionSecond.getX(),newPositionSecond.getY()) == True):
                self.actor.move(directionSecond.value)
            elif (self.getTile(newPositionThird.getX(),newPositionThird.getY()) == True):
                self.actor.move(directionThird.value)
            else:
                firstColumn = True
                self.buildPar(ax, drawer, firstColumn)


    def buildPar(self, ax, drawer, firstColumn):
        print(firstColumn)
        actorPosition = self.actor.getPosition()
        while(self.getTile(actorPosition.getX(),actorPosition.getY()) == True):
            drawer.draw_hex_grid(ax, self)
            plt.draw()
            plt.pause(1)
            if(self.actor.getPosition().getX() % 2 == 0):
                direction01 = coordinate.DirectionEven.SW
                direction02 = coordinate.DirectionEven.NE
                direction03 = coordinate.DirectionEven.SE
                direction04 = coordinate.DirectionEven.N
                direction05 = coordinate.DirectionEven.NW
                direction06 = coordinate.DirectionEven.S
            else:
                direction01 = coordinate.DirectionOdd.SW
                direction02 = coordinate.DirectionOdd.NE
                direction03 = coordinate.DirectionOdd.SE
                direction04 = coordinate.DirectionOdd.N
                direction05 = coordinate.DirectionOdd.NW
                direction06 = coordinate.DirectionOdd.S
            newPosition01 = actorPosition.mix(direction01.value)
            newPosition02 = actorPosition.mix(direction02.value)
            newPosition03 = actorPosition.mix(direction03.value)
            newPosition04 = actorPosition.mix(direction04.value)
            if(firstColumn and self.getTile(newPosition01.getX(),newPosition01.getY()) == True):
                self.actor.move(direction01.value)
            elif(self.getTile(newPosition02.getX(),newPosition02.getY()) == True and self.getTile(newPosition03.getX(),newPosition03.getY()) == False):
                self.actor.move(direction03.value)
                self.actor.move(direction05.value)
            elif(self.getTile(newPosition04.getX(),newPosition04.getY()) == True and self.getTile(newPosition03.getX(),newPosition03.getY()) == True and self.getTile(newPosition02.getX(),newPosition02.getY()) == False):
                self.actor.move(direction02.value)
                self.actor.move(direction01.value)
            else:
                self.actor.move(direction06.value)
        if(self.actor.getPosition().getX() % 2 == 0):
            direction01 = coordinate.DirectionEven.N
            direction02 = coordinate.DirectionEven.NE
            direction03 = coordinate.DirectionEven.SE
        else:
            direction01 = coordinate.DirectionOdd.N
            direction02 = coordinate.DirectionOdd.NE
            direction03 = coordinate.DirectionOdd.SE
        newPosition01 = actorPosition.mix(direction01.value)
        newPosition02 = actorPosition.mix(direction02.value)
        newPosition03 = actorPosition.mix(direction03.value)
        if(self.getTile(newPosition01.getX(),newPosition01.getY()) == True and self.getTile(newPosition02.getX(),newPosition02.getY()) == True and self.getTile(newPosition03.getX(),newPosition03.getY()) == True):
            self.actor.move(direction01.value)
        elif(self.getTile(newPosition02.getX(),newPosition02.getY()) == True):
            self.actor.move(direction02.value)
            self.actor.move(direction01.value)
            firstColumn = False



            
    
                