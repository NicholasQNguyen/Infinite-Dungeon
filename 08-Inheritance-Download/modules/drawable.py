import os
import pygame
from .vector2D import Vector2

class Drawable(object):
 
    WINDOW_OFFSET = Vector2(0, 0)

    @classmethod
    def updateWindowOffset(cls, tracked, screenSize, worldSize):
        position = tracked.getPosition()
        size = tracked.getSize()
        width = size[0]
        height = size[1]
        Drawable.WINDOW_OFFSET = Vector2(min(max(0, position[0] + (width // 2) - (screenSize[0] // 2)),
                        worldSize[0] - screenSize[0]),
                    min(max(0, position[1] + (height // 2) - (screenSize[1] // 2)),
                        worldSize[1] - screenSize[1]))
    
    _imageName = None
    _image = None
    _position = Vector2 (0, 0)

    def __init__(self, imageName, position):
        self._imageName = imageName
        self._position = Vector2(0, 0)
        self._image = pygame.image.load(os.path.join("images", self._imageName)).convert()         
        background = pygame.image.load(os.path.join("images", "background.png")).convert()

    def getPosition(self):
        return self._position

    def setPosition(self, newPosition):
        self._position = newPosition
      
    def getSize(self):
        return self._image.get_size()

    def getCollisionRect(self):
        newRect =  self._position + self._image.get_rect()
        return newRect
   
    def draw(self, surface):
        surface.blit(self._image, list(self._position - Drawable.WINDOW_OFFSET))


