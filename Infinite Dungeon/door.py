"""
Author: Nicholas Nguyen
Final Project
File: door.py

Class to handle doors and room transitions
"""

from vector2D import Vector2
from drawable import Drawable


class Door(Drawable):

    def __init__(self, cardinalDirection, destination):
        # Place it on the North wall
        if cardinalDirection == "North":        # Half the width of the room
            super().__init__("door.png", Vector2(504, 0))
            self.type = cardinalDirection
        elif cardinalDirection == "East":
            super().__init__("door.png", Vector2((1008 - 64), 504))
            self._position = Vector2((1008 - 64), 504)
        elif cardinalDirection == "South":
            super().__init__("door.png", Vector2(504, (1008 - 54)))
            self._position = Vector2(504, (1008 - 54))
        elif cardinalDirection == "West":
            super().__init__("door.png", Vector2(0, 504))
            self._position = Vector2(0, 504)

        # Room id number of where it leads
        self._destination = destination
        self.type = cardinalDirection
    def getDestination(self):
        """Transition from one room to another"""
        return self._destination

    def getPosition(self):
        return self._position