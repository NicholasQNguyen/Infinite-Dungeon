
from .vector2D import Vector2
from .drawable import Drawable
import pygame
import math
import random

class Tree(Drawable):
   
   def __init__(self, position, surfaceSize=Vector2(200,200), parallax=1):
      super().__init__("", position, parallax=parallax)
      
      
      self._angle = 75
      self._trunkSize = 50 
      self._branchSize = 20 
      self._branchNumber = 4
      self._levels = 3
      self._trunkWidth = 3
      self._barkColor = (random.randint(50,255),
                         random.randint(0,20),
                         random.randint(10,30))
      self._leafColor = (20,200,50)
      
      self._image = pygame.Surface(list(surfaceSize), pygame.SRCALPHA)
      
      self._drawSelf()
   
   def _drawSelf(self):
      
      startPoint = Vector2(self._image.get_width() // 2, self._image.get_height())
      startVector = Vector2(0, -1)
      angle = self._angle * math.pi / 180
      
      pygame.draw.line(self._image, self._barkColor, list(startPoint), list(startPoint + startVector * self._trunkSize), self._trunkWidth)
      
      def recurse(position, heading, level, size):
         if level == 0:
            pygame.draw.circle(self._image, self._leafColor, list(map(int,position)), 2)
         
         else:
            heading.rotate(-angle / 2)
            for branch in range(self._branchNumber):
               nextPos = position + heading * size
               pygame.draw.line(self._image, self._barkColor, list(map(int,position)), list(map(int,nextPos)), self._trunkWidth - (self._levels - level))
               recurse(nextPos, Vector2(*heading), level-1, size)
               heading.rotate(angle / (self._branchNumber - 1))
                  
      
      recurse(startPoint + startVector * self._trunkSize, startVector, self._levels, self._branchSize)
      
      

      
      
      
   
   