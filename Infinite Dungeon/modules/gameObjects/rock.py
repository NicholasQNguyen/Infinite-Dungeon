"""
Author: Nicholas Nguyen
Final Project
File: rock.py

Class to handle randomly placed rocks.
"""
import pygame

from .drawable import Drawable


class Rock(Drawable):

    def __init__(self, position):
        super().__init__("rock.png", position, None)

    def getCollideRect(self):
        """Returns the collision area of the object"""
        rect = self._position + pygame.Rect(self._image.get_rect())
        return rect
