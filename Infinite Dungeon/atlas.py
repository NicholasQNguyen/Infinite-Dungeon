"""
Author: Nicholas Nguyen
Final Porject
File: atlas.py


A class to hold onto and manage rooms
"""

from vector2D import Vector2
from random import randint, choice
from room import Room


DIMENSION = 6
ROOM_TYPES = ["basicRoom.png", "bridgeRoom.png", "torchRoom.png"]

class Atlas(object):

    def __init__(self):
        self.atlas = []
        for i in range(DIMENSION):
            self.atlas.append([])

        self.roomAssignment = 1

        # Make a DIMENSIONxDIMENSION grid to represent the map
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

"""
            The map looks like this:
            [0, 0, 0]
            [0, 0, 0]
            [0, 0, 0]

            These methods check for 1's above,
            to the right, below, and to the left
            of the inputted index
"""

