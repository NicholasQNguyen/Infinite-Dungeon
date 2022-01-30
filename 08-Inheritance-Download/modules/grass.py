
import pygame

from .vector2D import Vector2
import os
from .drawable import Drawable
   

class Grass(Drawable):
   """Grass does not move but can change its image."""
   def __init__(self, position):
     
      super().__init__("flowers-color-key.png", position)

      self._image = pygame.image.load(os.path.join("images", self._imageName)).convert()         
      
      surf = pygame.Surface((114,116))
      surf.blit(self._image, (0,0), pygame.Rect(456,116,114,116))
      
      self._image = surf
      
      self._image.set_colorkey(self._image.get_at((0,0)))

      self._position = position
      
      self._grassImage = self._image
      
      image = pygame.image.load(os.path.join("images", self._imageName)).convert()
         
      self._roseImage = pygame.Surface((114,116))
      self._roseImage.blit(image, (0,0), pygame.Rect(342,232,114,116))
      
      self._roseImage.set_colorkey(self._image.get_at((0,0)))

   def changeToRose(self):
      self._image = self._roseImage
      
   def changeToGrass(self):
      self._image = self._grassImage
      
   

   
   
   
      
