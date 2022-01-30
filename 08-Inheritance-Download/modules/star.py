import pygame
import os
from modules.vector2D import Vector2
from .mobile import Mobile


class Star(Mobile):
   """A movable rose based on WASD"""
   def __init__(self, position):
      
      super().__init__("star.png", position)

      self._image = pygame.image.load(os.path.join("images", self._imageName)).convert()
      
      self._image.set_colorkey(self._image.get_at((0,0)))

      self._position = position
      
      self.speed = 500
      self._velocity = Vector2(0,0)
   
   def handleEvent(self, event):
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_DOWN:
            self._velocity[1] = self.speed
         elif event.key == pygame.K_UP:
            self._velocity[1] = -self.speed
         elif event.key == pygame.K_LEFT:
            self._velocity[0] = -self.speed
         elif event.key == pygame.K_RIGHT:
            self._velocity[0] = self.speed
      
      elif event.type == pygame.KEYUP:
         if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
            self._velocity[1] = 0
         elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            self._velocity[0] = 0
