"""
Author: Nicholas Nguyen
Project 2
File: drawable.py
"""

import pygame
import os


class Drawable(object):

    def __init__(self, imageName, position):
        self._imageName = imageName
        self._image = pygame.image.load(
                      os.path.join("images", self._imageName)).convert_alpha()

        self._position = position

    def draw(self, surface, offset):
        """Blits the orb onto a specifed surface with an offset"""
        surface.blit(self._image, list(self._position - offset))

    def getSize(self):
        """Returns the size of the surface"""
        return self._image.get_size()

    def getWidth(self):
        """Returns the width of the surface as an int"""
        return self._image.get_width()

    def getHeight(self):
        """Returns the width of the surface as an int"""
        return self._image.get_height()

    def getCollideRect(self):
        """Returns the collision area of the object"""
        return self._position + pygame.Rect(self._image.get_rect())
