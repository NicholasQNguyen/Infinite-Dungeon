"""
Author: Nicholas Nguyen
Project 2
File: drawable.py

Class to handle things that can be drawn (characters, UI, etc.)
"""

import pygame
from .vector2D import Vector2
from ..managers.frameManager import FrameManager
from ..FSMs.basicFSM import BasicState


class Drawable(object):

    WINDOW_OFFSET = Vector2(0, 0)

    @classmethod
    def updateWindowOffset(cls, tracked, screenSize, worldSize):
        position = tracked.getPosition()
        size = tracked.getSize()
        width = size[0]
        length = size[1]
        Drawable.WINDOW_OFFSET = Vector2(min(max(0, position[0] + (width // 2)
                                             - (screenSize[0] // 2)),
                                         worldSize[0] - screenSize[0]),

                                         min(max(0, position[1] + (length // 2)
                                             - (screenSize[1] // 2)),
                                         worldSize[1] - screenSize[1]))

    @classmethod
    def setWindowOffset(cls, newOffset):
        Drawable.WINDOW_OFFSET = newOffset

    def __init__(self, imageName, position, offset=None):
        self._imageName = imageName

        frameManager = FrameManager.getInstance()

        if self._imageName != "":
            self._image = frameManager.getFrame(self._imageName, offset)

        self._position = Vector2(*position)
        self._state = BasicState()

    def draw(self, surface):
        """Blits the character onto a specifed surface with an offset"""
        blitImage = self._image

        if self._state.getFacing() == "left":
            blitImage = pygame.transform.flip(self._image, True, False)

        surface.blit(blitImage, list(self._position -
                                     Drawable.WINDOW_OFFSET))

        pygame.draw.rect(surface, (0, 0, 255), 
                         Drawable.WINDOW_OFFSET + self.getCollideRect(), 2)

    def setImage(self, surface):
        self._image = surface

    def setPosition(self, newPosition):
        self._position = newPosition

    def getPosition(self):
        return self._position

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
