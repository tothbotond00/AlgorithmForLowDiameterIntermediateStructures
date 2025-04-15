import actor_console as actor
import coordinate_console as coordinate

class Plane:
    actor = actor.Actor(0,0)
    tiles = []
    x = 0
    y = 0
    
    def __init__(self, x, y, filename, tile_counter):
        self.x = x
        self.y = y
        for i in range(x):
            helper = []
            for j in range(y):
                helper.append(False)
            self.tiles.append(helper)
            
        # Open the file in read mode
        with open(f'./tests100/{filename}', 'r') as file:
        # Iterate through each line in the file
            i = 0
            for line in file:
                for j in range(len(line)):
                    #If 1 then it is a simple Tile
                    if line[j] != '\n' and int(line[j]) == 1:
                        self.tiles[j][i] = True
                        tile_counter[0] += 1
                    #If two then it is a simple tile with the actor
                    if line[j] != '\n' and int(line[j]) == 2:
                        self.tiles[j][i] = True
                        tile_counter[0] += 1
                        self.actor = actor.Actor(j,i)
                i += 1

        self.firstColumn = True
        
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
    
    def placeTile(self):
        if self.actor.hasTile:
            self.tiles[self.actor.getPosition().getX()][self.actor.getPosition().getY()] = True
            self.actor.hasTile = False

    def pickupTile(self, moved_tiles_counter):
        self.tiles[self.actor.getPosition().getX()][self.actor.getPosition().getY()] = False
        self.actor.hasTile = True
        moved_tiles_counter[0] += 1


    # Moves the Actor to the proper coordinate based on a random direction (For testing purpose only)
    def moveActor(self, step_counter, moved_tiles_counter):

        while True:

            direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
            actorPosition = self.actor.getPosition()

            newPosition01 = actorPosition.mix(direction05.value)
            newPosition02 = actorPosition.mix(direction06.value)
            newPosition03 = actorPosition.mix(direction01.value)

            if(self.getTile(newPosition01.getX(),newPosition01.getY()) == True):
                self.actor.move(direction05.value, step_counter)
            elif (self.getTile(newPosition02.getX(),newPosition02.getY()) == True):
                self.actor.move(direction06.value, step_counter)
            elif (self.getTile(newPosition03.getX(),newPosition03.getY()) == True):
                self.actor.move(direction01.value, step_counter)
            else:
                self.firstColumn = True
                self.buildPar(step_counter)

                direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
                actorPosition = self.actor.getPosition()

                if(self.getTile(actorPosition.getX(),actorPosition.getY()) == False):
                    return
                elif(self.actor.hasTile == False):
                    newPosition01 = actorPosition.mix(direction01.value)
                    newPosition02 = actorPosition.mix(direction02.value)
                    newPosition03 = actorPosition.mix(direction05.value)
                    newPosition04 = actorPosition.mix(direction06.value)

                    if(self.firstColumn == True):
                        while(self.getTile(newPosition01.getX(),newPosition01.getY()) == True):
                            self.actor.move(direction01.value, step_counter)
                            direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
                            actorPosition = self.actor.getPosition()
                            newPosition01 = actorPosition.mix(direction01.value)
                    else:
                        while(self.getTile(newPosition02.getX(),newPosition02.getY()) == True or self.getTile(newPosition04.getX(),newPosition04.getY()) == True):
                            if(self.getTile(newPosition04.getX(),newPosition04.getY()) == True):
                                self.actor.move(direction06.value, step_counter)
                            elif(self.getTile(newPosition02.getX(),newPosition02.getY()) == True):
                                self.actor.move(direction02.value, step_counter)

                            direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
                            actorPosition = self.actor.getPosition()
                            newPosition01 = actorPosition.mix(direction01.value)
                            newPosition02 = actorPosition.mix(direction02.value)
                            newPosition03 = actorPosition.mix(direction05.value)
                            newPosition04 = actorPosition.mix(direction06.value)

                        while(self.getTile(newPosition01.getX(),newPosition01.getY()) == True or self.getTile(newPosition03.getX(),newPosition03.getY()) == True or self.getTile(newPosition04.getX(),newPosition04.getY()) == True):
                            if(self.getTile(newPosition03.getX(),newPosition03.getY()) == True):
                                self.actor.move(direction05.value, step_counter)
                            elif(self.getTile(newPosition04.getX(),newPosition04.getY()) == True):
                                self.actor.move(direction06.value, step_counter)
                            elif(self.getTile(newPosition01.getX(),newPosition01.getY()) == True):
                                self.actor.move(direction01.value, step_counter)

                            direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
                            actorPosition = self.actor.getPosition()
                            newPosition01 = actorPosition.mix(direction01.value)
                            newPosition03 = actorPosition.mix(direction05.value)
                            newPosition04 = actorPosition.mix(direction06.value)

                    direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
                    actorPosition = self.actor.getPosition()

                    newPosition01 = actorPosition.mix(direction02.value)
                    newPosition02 = actorPosition.mix(direction03.value)
                    newPosition03 = actorPosition.mix(direction04.value)

                    self.pickupTile(moved_tiles_counter)

                    if(self.getTile(newPosition01.getX(),newPosition01.getY()) == True):
                        self.actor.move(direction02.value, step_counter)

                    elif(self.getTile(newPosition02.getX(),newPosition02.getY()) == True):
                        self.actor.move(direction03.value, step_counter)

                    elif(self.getTile(newPosition03.getX(),newPosition03.getY()) == True):
                        self.actor.move(direction04.value, step_counter)

    def buildPar(self, step_counter):

        actorPosition = self.actor.getPosition()
        while(self.getTile(actorPosition.getX(),actorPosition.getY()) == True):

            direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
            
            newPosition01 = actorPosition.mix(direction06.value)
            newPosition02 = actorPosition.mix(direction03.value)
            newPosition03 = actorPosition.mix(direction04.value)
            newPosition04 = actorPosition.mix(direction01.value)
            if(self.firstColumn and self.getTile(newPosition01.getX(),newPosition01.getY()) == True):
                self.actor.move(direction06.value, step_counter)
                return
            elif(self.getTile(newPosition02.getX(),newPosition02.getY()) == True and self.getTile(newPosition03.getX(),newPosition03.getY()) == False):
                self.actor.move(direction04.value, step_counter)

                direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
                actorPosition = self.actor.getPosition()

                self.placeTile()
                self.actor.move(direction05.value, step_counter)
                return
            elif(self.getTile(newPosition04.getX(),newPosition04.getY()) == True and self.getTile(newPosition03.getX(),newPosition03.getY()) == True and self.getTile(newPosition02.getX(),newPosition02.getY()) == False):
                self.actor.move(direction03.value, step_counter)

                direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
                actorPosition = self.actor.getPosition()

                self.placeTile()
                self.actor.move(direction06.value, step_counter)
                return
            else:
                self.actor.move(direction02.value, step_counter)

        direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
        actorPosition = self.actor.getPosition()

        newPosition01 = actorPosition.mix(direction01.value)
        newPosition02 = actorPosition.mix(direction03.value)
        newPosition03 = actorPosition.mix(direction04.value)
        if(self.getTile(newPosition01.getX(),newPosition01.getY()) == True and self.getTile(newPosition02.getX(),newPosition02.getY()) == True and self.getTile(newPosition03.getX(),newPosition03.getY()) == True):
            self.placeTile()
            self.actor.move(direction01.value, step_counter)

        elif(self.getTile(newPosition02.getX(),newPosition02.getY()) == True):
            self.actor.move(direction03.value, step_counter)
            self.actor.move(direction01.value, step_counter)
            self.firstColumn = False

            while(self.getTile(actorPosition.getX(),actorPosition.getY()) == True):

                direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
                actorPosition = self.actor.getPosition()

                newPosition01 = actorPosition.mix(direction06.value)
                newPosition02 = actorPosition.mix(direction05.value)
                newPosition03 = actorPosition.mix(direction01.value)
                newPosition04 = actorPosition.mix(direction02.value)

                if(self.getTile(newPosition01.getX(),newPosition01.getY()) == False and self.getTile(newPosition02.getX(),newPosition02.getY()) == True):
                    while(self.getTile(newPosition03.getX(),newPosition03.getY()) == True):
                        self.actor.move(direction03.value, step_counter)

                        direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
                        actorPosition = self.actor.getPosition()
                        newPosition03 = actorPosition.mix(direction01.value)
                    while(self.getTile(newPosition02.getX(),newPosition02.getY()) == False):
                        self.actor.move(direction02.value, step_counter)

                        direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
                        actorPosition = self.actor.getPosition()
                        newPosition02 = actorPosition.mix(direction05.value)

                    return
                else:
                    self.actor.move(direction01.value, step_counter)

            direction01, direction02, direction03, direction04, direction05, direction06 = self.getDirections()
            actorPosition = self.actor.getPosition()

            newPosition01 = actorPosition.mix(direction02.value)
            newPosition02 = actorPosition.mix(direction04.value)
            if(self.getTile(newPosition01.getX(),newPosition01.getY()) == True and self.getTile(newPosition02.getX(),newPosition02.getY()) == True):
                self.placeTile()

            else:
                self.actor.move(direction02.value, step_counter)
                self.buildPar(step_counter)

        return

    def printState(self):
        return_string = ""
        for i in range(self.x):
            for j in range(self.y):
                if(self.tiles[j][i]) == True :
                    return_string += "1"
                else:
                    return_string += "0"
            return_string += "\n"
        for i in range(self.x):
            for j in range(self.y):
                self.tiles[j][i] = False
        return return_string