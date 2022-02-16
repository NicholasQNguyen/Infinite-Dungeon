

from .drawable import Drawable
from .vector2D import Vector2

import pygame
import math


def calculateAngle(pos1, pos2):
   # Returns in radians
   triangle = pos2 - pos1
   addition = 0
   
   if triangle.x == 0:
      addition = math.pi / 2
   else:
      addition += math.atan(triangle.y / triangle.x)
      
   if triangle.x > 0:
       return math.pi - addition
   if triangle.y < 0:
      return math.pi * 2 - addition
   return -addition


class Rotatable(Drawable):
   
   # Debug flag
   DEBUG_DRAW = True
   
   def __init__(self, imageName, position, offset=None):
      super().__init__(imageName, position, offset)

      # Keep track of the actual position so that drawable's draw still works
      self._truePosition = Vector2(*position)
      self._unrotatedImage = self._image
      
      # Rotation angle
      self._angle = 0
      
      self._pivot = None
   
   def setRotated(self):   
      # Calculate degrees because pygame.transform.rotate expects degrees
      degrees = self._angle * 180 / math.pi
      center = Vector2(*self._unrotatedImage.get_rect().center)   
      
      # Rotate the surface in its own variable
      rotatedSurface = pygame.transform.rotate(self._unrotatedImage, degrees)
      self._image = rotatedSurface
      
      # Move the relative distance from the rotated surface's offset to find the offset's rotated position on the surface
      if self._pivot != None:
         rotatedOffset = self._pivot - self.getRotatedPivot()
      else:
         rotatedOffset = center - Vector2(*rotatedSurface.get_rect().center) 
      
      # find the new world coordinates based on the old coordinates, moved to the pivot, moved back by the rotated pivot position.   
      newBlit = self._truePosition + rotatedOffset
      
      self._position = newBlit
      
   def getRotatedPivot(self, pivot=None):
      center = Vector2(*self._unrotatedImage.get_rect().center)
      
      # Allow for a unique pivot for hinge calculations
      if pivot == None:
         pivot = self._pivot
      
      # Obtain a vector representing the relative distance between the center and the pivot
      pivotToCenter = Vector2(*center) - pivot
      
      # Rotate the relative distance between center and pivot
      pivotToCenterRotated = Vector2(*pivotToCenter)
      pivotToCenterRotated.rotate(-self._angle)
      
      # Find the new center of the rotated surface
      centerRotated = Vector2(*self._image.get_rect().center)
      
      # Move the relative distance from the rotated surface's center to find the pivot's rotated position on the surface
      pivotRotated = centerRotated - pivotToCenterRotated
      
      return pivotRotated
   
   
   def setPivot(self, pivot):
      self._pivot = Vector2(*pivot)
      self.setRotated()
      
   def getPivot(self):
      return self._pivot
   
   def setTruePosition(self, position):
      self._truePosition = Vector2(*position)
   
   def getTruePosition(self):
      return self._truePosition

   def setPosition(self, position):
      self.setTruePosition(position)
      self.setRotated()
      
   def getPosition(self):
      return self.getTruePosition()
   
   def getHiddenPosition(self):
      return self._position
   
   def setPivotPosition(self, position):      
      self.setTruePosition(position - self.getPivot())
      self.setRotated()
   
   def setImage(self, surface):
      self._unrotatedImage = surface
      self.setRotated()
   
   
   def getAngle(self):
      return self._angle
   
   def draw(self, surface):     
      super().draw(surface)
      
      # Debugs
      if Rotatable.DEBUG_DRAW:
         pygame.draw.rect(surface, (0,255,0), self._position + self._image.get_rect(), 1)
         if self._pivot != None:
            pin = self._position + self.getRotatedPivot()
         else:
            pin = self._position + Vector2(*self._image.get_rect().center)
         # pygame.draw.circle(surface, (0,255,0), list(map(int, pin)), 2)
         pygame.draw.circle(surface, (0,255,0), list(map(int, pin)), 2)
         
   def getCenter(self):
      return self._image.get_rect().center

   def increaseAngle(self):
      self._angle += math.pi / 16
      
   def decreaseAngle(self):
      self._angle -= math.pi / 16
      
   def pointToPosition(self, pos):
      self._angle = calculateAngle(pos, (self.getHiddenPosition() + Vector2(*self.getCenter())))
      self.setRotated()
      
   
   
         
      

      