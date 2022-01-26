"""
Author: Nicholas Nguyen
Project 2
File: mobile.py
"""
from drawable import Drawable


class Mobile(Drawable):

    def __init__(self, position, velocity, imageName):
        super().__init__(imageName, position)
        self._velocity = velocity

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


