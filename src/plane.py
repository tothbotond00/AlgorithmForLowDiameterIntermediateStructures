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
    
    def getDirections(self):
        if(self.actor.getPosition().getX() % 2 == 0):
            direction01 = coordinate.DirectionEven.N
            direction02 = coordinate.DirectionEven.S
            direction03 = coordinate.DirectionEven.NE
            direction04 = coordinate.DirectionEven.SE
            direction05 = coordinate.DirectionEven.NW
            direction06 = coordinate.DirectionEven.SW
        else:
            direction01 = coordinate.DirectionOdd.N
            direction02 = coordinate.DirectionOdd.S
            direction03 = coordinate.DirectionOdd.NE
            direction04 = coordinate.DirectionOdd.SE
            direction05 = coordinate.DirectionOdd.NW
            direction06 = coordinate.DirectionOdd.SW
        return direction01, direction02, direction03, direction04, direction05, direction06
    
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

            direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
            actorPosition = self.actor.getPosition()

            newPosition01 = actorPosition.mix(direction05.value)
            newPosition02 = actorPosition.mix(direction06.value)
            newPosition03 = actorPosition.mix(direction01.value)

            if(self.getTile(newPosition01.getX(),newPosition01.getY()) == True):
                self.actor.move(direction05.value)
            elif (self.getTile(newPosition02.getX(),newPosition02.getY()) == True):
                self.actor.move(direction06.value)
            elif (self.getTile(newPosition03.getX(),newPosition03.getY()) == True):
                self.actor.move(direction01.value)
            else:
                firstColumn = True
                self.buildPar(ax, drawer, firstColumn)

                

            drawer.draw_hex_grid(ax, self)
            plt.draw()
            plt.pause(1)


    def buildPar(self, ax, drawer, firstColumn):

        actorPosition = self.actor.getPosition()
        while(self.getTile(actorPosition.getX(),actorPosition.getY()) == True):

            direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
            
            newPosition01 = actorPosition.mix(direction06.value)
            newPosition02 = actorPosition.mix(direction03.value)
            newPosition03 = actorPosition.mix(direction04.value)
            newPosition04 = actorPosition.mix(direction05.value)
            if(firstColumn and self.getTile(newPosition01.getX(),newPosition01.getY()) == True):
                self.actor.move(direction06.value)
            elif(self.getTile(newPosition02.getX(),newPosition02.getY()) == True and self.getTile(newPosition03.getX(),newPosition03.getY()) == False):
                self.actor.move(direction04.value)
                self.actor.move(direction05.value)
            elif(self.getTile(newPosition04.getX(),newPosition04.getY()) == True and self.getTile(newPosition03.getX(),newPosition03.getY()) == True and self.getTile(newPosition02.getX(),newPosition02.getY()) == False):
                self.actor.move(direction03.value)
                self.actor.move(direction06.value)
            else:
                self.actor.move(direction02.value)

            drawer.draw_hex_grid(ax, self)
            plt.draw()
            plt.pause(1)

        direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
        actorPosition = self.actor.getPosition()

        newPosition01 = actorPosition.mix(direction01.value)
        newPosition02 = actorPosition.mix(direction03.value)
        newPosition03 = actorPosition.mix(direction04.value)
        if(self.getTile(newPosition01.getX(),newPosition01.getY()) == True and self.getTile(newPosition02.getX(),newPosition02.getY()) == True and self.getTile(newPosition03.getX(),newPosition03.getY()) == True):
            self.actor.move(direction01.value)
            drawer.draw_hex_grid(ax, self)
            plt.draw()
            plt.pause(1)
        elif(self.getTile(newPosition02.getX(),newPosition02.getY()) == True):
            self.actor.move(direction03.value)
            drawer.draw_hex_grid(ax, self)
            plt.draw()
            plt.pause(1)
            self.actor.move(direction01.value)
            drawer.draw_hex_grid(ax, self)
            plt.draw()
            plt.pause(1)

            firstColumn = False
        while(self.getTile(actorPosition.getX(),actorPosition.getY()) == True):

            direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
            actorPosition = self.actor.getPosition()

            newPosition01 = actorPosition.mix(direction06.value)
            newPosition02 = actorPosition.mix(direction05.value)
            newPosition03 = actorPosition.mix(direction01.value)
            newPosition04 = actorPosition.mix(direction02.value)

            if(self.getTile(newPosition01.getX(),newPosition01.getY()) == True and self.getTile(newPosition02.getX(),newPosition02.getY()) == False):
                while(self.getTile(newPosition03.getX(),newPosition03.getY()) == True):
                    self.actor.move(direction03.value)

                    drawer.draw_hex_grid(ax, self)
                    plt.draw()
                    plt.pause(1)

                    direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
                    actorPosition = self.actor.getPosition()
                    newPosition03 = actorPosition.mix(direction01.value)
                while(self.getTile(newPosition02.getX(),newPosition02.getY()) == False):
                    self.actor.move(direction02.value)

                    drawer.draw_hex_grid(ax, self)
                    plt.draw()
                    plt.pause(1)

                    direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
                    actorPosition = self.actor.getPosition()
                    newPosition02 = actorPosition.mix(direction05.value)
            else:
                self.actor.move(direction01.value)
                drawer.draw_hex_grid(ax, self)
                plt.draw()
                plt.pause(1)

        direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
        actorPosition = self.actor.getPosition()

        newPosition01 = actorPosition.mix(direction02.value)
        newPosition02 = actorPosition.mix(direction04.value)
        if(self.getTile(newPosition01.getX(),newPosition01.getY()) == True and self.getTile(newPosition02.getX(),newPosition02.getY()) == True):
            self.actor.move(direction02.value)
            drawer.draw_hex_grid(ax, self)
            plt.draw()
            plt.pause(1)

        else:
            self.actor.move(direction02.value)
            drawer.draw_hex_grid(ax, self)
            plt.draw()
            plt.pause(1)

            self.buildPar(ax, drawer, firstColumn)





            
    
                