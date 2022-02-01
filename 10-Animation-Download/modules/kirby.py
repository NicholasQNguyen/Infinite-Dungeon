import pygame

from .mobile import Mobile
from .animated import Animated
from .vector2D import Vector2
import os

   
class Kirby(Animated):
   def __init__(self, position):
      super().__init__("kirby.png", position)
      
      self._nFrames = 4
      
      self._row = 1
