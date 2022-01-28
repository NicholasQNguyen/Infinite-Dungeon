"""
Author: Nicholas Nguyen
Final Porject
File: atlas.py


A class to hold onto and manage rooms
"""

from vector2D import Vector2
from random import randint
from room import Room


class Atlas(object):

    atlas = [[], [], []]

    def __init__(self):
        # Make a 9x9 grid to represent the map
        for lyst in self.atlas:
            for i in range(3):
                # 1's means theres a room, 0's means there's not
                lyst.append(randint(0, 1))

        for lyst in self.atlas:
            for i in range(3):
                # Add rooms where there are 1's
                if lyst[i] == 1:
                    lyst[i] = Room("basicRoom.png",
                                   Vector2(0, 0), Room.currentRoomNumber)

            for i in range(3):
                if lyst[i] != 0:
                    if lyst[i].hasNorth:
                        lyst[i].setNorthDoor()

                    if lyst[i].hasEast:
                        lyst[i].setEastDoor()

                    if lyst[i].hasSouth:
                        lyst[i].setSouthDoor()

                    if lyst[i].hasWest:
                        lyst[i].setWestDoor()


"""
            The map looks like this:
            [0, 0, 0]
            [0, 0, 0]
            [0, 0, 0]

            These methods check for 1's above,
            to the right, below, and to the left
            of the inputted index

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
def main():
    atlas = Atlas()
    for lyst in atlas.atlas:
        print(lyst)
    print(atlas.hasLeftNeighbor((1,1)))

if __name__ == "__main__":
    main()
"""
