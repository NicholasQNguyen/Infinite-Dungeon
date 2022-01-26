"""
Author: Nicholas Nguyen
Project 2
File: drawable.py
"""

from vector2D import Vector2
import pygame


class Drawable:
    _isDead = False
    _imageName = ""
    _image = None
    _position = Vector2(0, 0)
    _velocity = Vector2(0, 0)

    def draw(self, surface, offset):
        """Blits the orb onto a specifed surface with an offset"""
        surface.blit(self._image, list(self._position - offset))

    def getWorldPosition(self):
        return self._worldPosition

    def setWorldPosition(self, newPosition):
        self._worldPosition = newPosition

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

    def getSize(self):
        """Returns the size of the surface the orb is on"""
        return self._image.get_size()

    def getWidth(self):
        """Returns the width of the surface as an int"""
        return self._image.get_width()

    def getHeight(self):
        """Returns the width of the surface as an int"""
        return self._image.get_height()

    def getCollideRect(self):
        """Returns the colleision area of the object"""
        return self._position + pygame.Rect(self._image.get_rect())

    def kill(self):
        self._isDead = True

    def isDead(self):
        return self._isDead
