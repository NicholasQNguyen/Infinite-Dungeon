"""
Author: Nicholas Nguyen
Final Porject
File: atlas.py


A class to hold onto and manage rooms
"""

from vector2D import Vector2
from random import randint, choice
from room import Room


DIMENSION = 5
ROOM_TYPES = ["basicRoom.png", "bridgeRoom.png", "torchRoom.png"]

class Atlas(object):

    def __init__(self):
        self.atlas = []
        # Make a DIMENSIONxDIMENSION grid to represent the map
        for i in range(DIMENSION):
            self.atlas.append([])
            for j in range(DIMENSION):
                self.atlas[i].append(0)

        prevRoom = 0
        roomAssignment = 1
        nextRoom = 2

        right = False
        up = False

        placerIndex1 = DIMENSION - 1
        placerIndex2 = 0

        firstRoom = Room(choice(ROOM_TYPES), 0, 1)
        lastRoom = Room(choice(ROOM_TYPES), 99)

        # Put a room in the bottom left and top right of the grid
        self.atlas[placerIndex1][placerIndex2] = firstRoom
        self.atlas[placerIndex2][placerIndex1] = lastRoom 

        # Keep adding rooms until we see the last room
        while isinstance(self.getNorth((placerIndex1, placerIndex2)), int) and \
              isinstance(self.getEast((placerIndex1, placerIndex2)), int):
            # From the bottom left room, go randomly right or up and put a room
            rightOrUp = randint(0,1)
            if rightOrUp == 0:
                right = True
            else:
                up = True

            if up:
                placerIndex1 -= 1
                # Account for if we're on the top edge of the map
                try:
                    newRoom = Room(choice(ROOM_TYPES), roomAssignment, prevRoom, nextRoom)
                    newRoom.setSouthDoor((roomAssignment - 1))
                    print("1:", placerIndex1, "2:", placerIndex2)
                    self.atlas[placerIndex1][placerIndex2] = newRoom
                    up = False
                    # Go to the previous room and add a door to link to the new room we just made
                    self.atlas[placerIndex1 + 1][placerIndex2].setNorthDoor(roomAssignment)
                # If we just get a bunch of up, then go right
                except IndexError:
                    placerIndex1 += 1
                    placerIndex2 += 1
                    newRoom = Room(choice(ROOM_TYPES), roomAssignment, prevRoom, nextRoom)
                    newRoom.setWestDoor(roomAssignment - 1)
                    print("1:", placerIndex1, "2:", placerIndex2)
                    self.atlas[placerIndex1][placerIndex2] = newRoom
                    # In the previous room, add a door to the east to match up with this room
                    self.atlas[placerIndex1][placerIndex2 - 1].setEastDoor(roomAssignment)

            else:
                placerIndex2 += 1
                # If we're on the right edge of the map
                try:
                    newRoom = Room(choice(ROOM_TYPES), roomAssignment, prevRoom, nextRoom)
                    newRoom.setWestDoor(roomAssignment - 1)
                    print("1:", placerIndex1, "2:", placerIndex2)
                    self.atlas[placerIndex1][placerIndex2] = newRoom
                    right = False
                    # In the previous room, add a door to the east to match up with this room
                    self.atlas[placerIndex1][placerIndex2 - 1].setEastDoor(roomAssignment)
                except IndexError:
                    placerIndex2 -= 1
                    placerIndex1 -= 1
                    newRoom = Room(choice(ROOM_TYPES), roomAssignment, prevRoom, nextRoom)
                    newRoom.setSouthDoor(roomAssignment - 1)
                    print("1:", placerIndex1, "2:", placerIndex2)
                    self.atlas[placerIndex1][placerIndex2] = newRoom
                    # Go to the previous room and add a door to link to the new room we just made
                    self.atlas[placerIndex1 + 1][placerIndex2].setNorthDoor(roomAssignment)
 
            roomAssignment += 1
            prevRoom += 1

        print("DONE LOOPING")
        # if we're one below the final room, add a door pointing up
        if self.getNorth((placerIndex1, placerIndex2)) == lastRoom:
            self.atlas[placerIndex1][placerIndex2].setNorthDoor(99)
            # add a door pointing back to the second to last room
            lastRoom.setSouthDoor(roomAssignment - 1)

        #If we're one to the left of the final room, add a door pointing right
        elif self.getEast((placerIndex1, placerIndex2)) == lastRoom:
            self.atlas[placerIndex1][placerIndex2].setEastDoor(99)
            lastRoom.setSouthDoor(roomAssignment - 1)

    def getRooms(self):
        """Get a list of the rooms in order.
           IE. [Room 0, Room 1, Room 2 etc.]"""
        listOfRooms = []
        for i in range(DIMENSION):
            for j in range(DIMENSION):
                if self.atlas[i][j] != 0:
                    listOfRooms.append(self.atlas[i][j])
        # We want a sorted list so that when we index in main, we get the right room
        return sorted(listOfRooms)

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

    def __str__(self):
        # https://stackoverflow.com/questions/50731788/str-to-give-a-visual-representation-of-the-2d-table-in-python
        return ('\n'.join(['|'.join([str(cell) for cell in row]) for row in self.atlas]))



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