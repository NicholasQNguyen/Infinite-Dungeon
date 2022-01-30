
import pygame

from .mobile import Mobile
from .drawable import Drawable
from .vector2D import Vector2
from .frameManager import FrameManager
   

class Grass(Drawable):
   """Grass does not move but can change its image."""
   def __init__(self, position):
      super().__init__("flowers-color-key.png", position, (4, 1))
      self._grassImage = self._image
      
      fm = FrameManager.getInstance()
 
      self._roseImage = fm.getFrame(self._imageName, (3, 2)) 
   
   def changeToRose(self):
      self.setImage(self._roseImage)
      
   def changeToGrass(self):
      self.setImage(self._grassImage)
      
   

   
   
   
      
