
import pygame

from .mobile import Mobile
from .animated import Animated
from .drawable import Drawable
from .vector2D import Vector2
import os

   
class Grass(Drawable):
   def __init__(self, position):
      super().__init__("flowers-color-key.png", position, (4, 1))
   
class WaterLilly(Animated):
   def __init__(self, position):
      super().__init__("water-lilly.png", position)
      
      self._nFrames = 5
      
      self._animate = False
      
   
   
   
   
      
   
   
      
