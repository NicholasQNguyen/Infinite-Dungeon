import pygame
from pygame import image
import os
from .frameManager import FrameManager
from .vector2D import Vector2

class Drawable(object):
   
   
   def __init__(self, imageName, position, offset=None):
      self._imageName = imageName

      # Let frame manager handle loading the image
      self._image = FrameManager.getInstance().getFrame(self._imageName, offset)

      self._position = Vector2(*position)
      
   def getPosition(self):
      return self._position

   def setPosition(self, newPosition):
      self._position = newPosition
      
   def getSize(self):
      return self._image.get_size()
   
   def setImage(self, surface):
      self._image = surface

   def getCollisionRect(self):
      newRect =  self._position + self._image.get_rect()
      return newRect
   
   def draw(self, surface):
      surface.blit(self._image, (self._position[0], self._position[1]))
     
