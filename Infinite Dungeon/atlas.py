"""
Author: Nicholas Nguyen
Final Porject
File: atlas.py


A class to hold onto and manage rooms
"""

from vector2D import Vector2
from random import randint, choice
from room import Room


DIMENSION = 3
ROOM_TYPES = ["basicRoom.png", "bridgeRoom.png", "torchRoom.png"]

class Atlas(object):

    def __init__(self):
        self.atlas = []
        # Make a DIMENSIONxDIMENSION grid to represent the map
        for i in range(DIMENSION):
            self.atlas.append([])
            for j in range(DIMENSION):
                self.atlas[i].append(0)
        
        roomAssignment = 1
        prevRoom = 0

        right = False
        up = False

        placerIndex1 = DIMENSION - 1
        placerIndex2 = 0

        firstRoom = Room(choice(ROOM_TYPES), 0, 1, east=True)
        lastRoom = Room(choice(ROOM_TYPES), 99)

        # Put a room in the bottom left and top right of the grid
        print(placerIndex1)
        print(placerIndex2)
        self.atlas[placerIndex1][placerIndex2] = firstRoom
        self.atlas[placerIndex2][placerIndex1] = lastRoom 

        print("North:", self.getNorth((placerIndex1, placerIndex2)))
        print("East:", self.getEast((placerIndex1, placerIndex2)))

        # Keep adding rooms until we see the last room
        while isinstance(self.getNorth((placerIndex1, placerIndex2)), int) or \
              isinstance(self.getEast((placerIndex1, placerIndex2)), int):
            # From the bottom left room, go randomly right or up and put a room
            rightOrUp = randint(0,1)
            if rightOrUp == 0:
                right = True
            else:
                up = True

            if up:
                placerIndex1 -= 1
                try:
                    newRoom = Room(choice(ROOM_TYPES), roomAssignment, prevRoom)
                    newRoom.setSouthDoor((roomAssignment - 1))
                    print("1:", placerIndex1, "2:", placerIndex2)
                    self.atlas[placerIndex1][placerIndex2] = newRoom
                # If we just get a bunch of up, then go right
                except IndexError:
                    placerIndex1 += 1
                    placerIndex2 += 1
                    newRoom = Room(choice(ROOM_TYPES), roomAssignment, prevRoom)
                    newRoom.setWestDoor(roomAssignment - 1)
                    print("1: ", placerIndex1, "2:", placerIndex2)
                    self.atlas[placerIndex1][placerIndex2] = newRoom

            else:
                placerIndex2 += 1
                try:
                    newRoom = Room(choice(ROOM_TYPES), roomAssignment, prevRoom)
                    newRoom.setWestDoor(roomAssignment - 1)
                    print("1: ", placerIndex1, "2:", placerIndex2)
                    self.atlas[placerIndex1][placerIndex2] = newRoom
                except IndexError:
                    placerIndex2 -= 1
                    placerIndex1 -= 1
                    newRoom = Room(choice(ROOM_TYPES), roomAssignment, prevRoom)
                    newRoom.setWestDoor(roomAssignment - 1)
                    print("1: ", placerIndex1, "2:", placerIndex2)
                    self.atlas[placerIndex1][placerIndex2] = newRoom

            roomAssignment += 1
            prevRoom += 1
            print("North:", self.getNorth((placerIndex1, placerIndex2)))
            print("East:", self.getEast((placerIndex1, placerIndex2)))


        # if we're one below the final room, add a door pointing up
        if self.atlas[placerIndex1][placerIndex2] == lastRoom:
            self.atlas[placerIndex1 - 1][placerIndex2].setNorthDoor(99)
            # add a door pointing back to the second to last room
            lastRoom.setSouthDoor(roomAssignment - 1)

        #If we're one to the left of the final room, add a door pointing right
        elif self.atlas[placerIndex1][placerIndex2] == lastRoom:
            self.atlas[placerIndex1][placerIndex2 - 1].setEastDoor(99)
            lastRoom.setSouthDoor(roomAssignment - 1)

    def getRooms(self):
        """Get a list of the rooms"""
        listOfRooms = []
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if self.atlas[i][j] != 0:
                    listOfRooms.append(self.atlas[i][j])
        return listOfRooms

    def hasNorth(self, indeces):
        try:
            return bool(self.atlas[indeces[0]-1][indeces[1]])
        except IndexError:
            return False

    def hasEast(self, indeces):
        try:
            return bool(self.atlas[indeces[0]][indeces[1]+1])
        except IndexError:
            return False

    def hasWest(self, indeces):
        try:
            return bool(self.atlas[indeces[0]][indeces[1]-1])
        except IndexError:
            return False

    def hasSouth(self, indeces):
        try:
            return bool(self.atlas[indeces[0]+1][indeces[1]])
        except IndexError:
            return False

    def getNorth(self, indeces):
        try:
            return self.atlas[indeces[0]-1][indeces[1]]
        except IndexError:
            return None

    def getEast(self, indeces):
        try:
            return self.atlas[indeces[0]][indeces[1] + 1]
        except IndexError:
            return None

"""
            The map looks like this:
            [0, 0, 0]
            [0, 0, 0]
            [0, 0, 0]

            These methods check for 1's above,
            to the right, below, and to the left
            of the inputted index
"""
"""
        for lyst in self.atlas:
            for i in range(DIMENSION):
                # 1's means theres a room, 0's means there's not
                lyst.append(randint(0, 1))

        for i in range(DIMENSION):
            for j in range(DIMENSION):
                # Add rooms where there are 1's
                if self.atlas[i][j] == 1:
                    self.atlas[i][j] = Room(choice(ROOM_TYPES),
                                            self.roomAssignment,
                                            north = choice((True, False)),
                                            east = choice((True, False)),
                                            south = choice((True, False)),
                                            west = choice((True, False)))
                    self.roomAssignment += 1
    

            for j in range(DIMENSION):
                if self.atlas[i][j] != 0:
                    if self.hasNorth((i, j)):
                        self.atlas[i][j].setNorthDoor()

                    if self.hasEast((i,j)):
                        self.atlas[i][j].setEastDoor()

                    if self.hasSouth((i, j)):
                        self.atlas[i][j].setSouthDoor()

                    if self.hasWest((i, j)):
                        self.atlas[i][j].setWestDoor()
"""
