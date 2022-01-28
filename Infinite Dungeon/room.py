"""
Author: Nicholas Nguyen
Final Project
File: room.py
"""

from vector2D import Vector2
from drawable import Drawable
from door import Door


class Room(Drawable):
    currentRoomNumber = 1
    _rooms = []

    def __init__(self, imageName, roomNumber,
                 north=False, east=False, south=False, west=False):
        super().__init__(imageName, Vector2(0, 0))
        # Dictionary to hold where there are paths
        self._doorLocations = {"North": north, "East": east,
                               "South": south, "West": west}
        self.doors = []

        # room ID number to allow for blitting of the right one
        self._roomNumber = roomNumber

        for key in self._doorLocations:
            if self._doorLocations[key]:
                self.doors.append(Door(key, self.currentRoomNumber))
                self.currentRoomNumber += 1

    def setNorthDoor(self):
        self._doorLocations["North"] = True

    def setEastDoor(self):
        self._doorLocations["East"] = True

    def setSouthDoor(self):
        self._doorLocations["South"] = True

    def setWestDoor(self):
        self._doorLocations["West"] = True

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


"""
        for key in self._doorLocations:
            # given the previousRoom, make a corresponding door
            if key == prevDirection:
                self._doorLocations[key] = True
            # otherwise randomize if there'll be a door or not
            else:
                self._doorLocations[key] = random.choice([True, False])

        for key in self._doorLocations:
            if self._doorLocations[key] == True:
                self.doors.append(Door(key, self._currentRoomNumber))
                self._currentRoomNumber += 1
"""
