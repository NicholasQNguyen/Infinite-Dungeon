"""
Author: Nicholas Nguyen
Project 2
File: mobile.py

Class for thing that can move and have a position and velocity
"""
from .animated import Animated
from .vector2D import Vector2


class Mobile(Animated):

    def __init__(self, imageName, position, offset=(0, 0)):
        super().__init__(imageName, position, offset)

    def getPosition(self):
        """Returns the Vector2 of the position"""
        return self._position

    def setPosition(self, newPosition):
        """Sets the new position"""
        self._position = newPosition

    def getX(self):
        """Returns the X position which is an int"""
        return self._position[0]

    def getY(self):
        """Returns the X position which is an int"""
        return self._position[1]

    def update(self, seconds):
        super().update(seconds)
        self._velocity = Vector2(0, 0)
        if self._state.getState() != "standing":
            # currentFacing = self._state.getFacing()

            if self._state._movement["down"]:
                self._velocity[1] = self._vspeed
            elif self._state._movement["up"]:
                self._velocity[1] = -self._vspeed
            if self._state._movement["left"]:
                self._velocity[0] = -self._vspeed
            elif self._state._movement["right"]:
                self._velocity[0] = self._vspeed

            newPosition = self.getPosition() + self._velocity * seconds
            self.setPosition(newPosition)

        else:
            self._velocity = Vector2(0, 0)
