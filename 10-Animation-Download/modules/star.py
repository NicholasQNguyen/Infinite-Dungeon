from .mobile import Mobile
import pygame

class Star(Mobile):
   """A movable rose based on WASD"""
   def __init__(self, position):
      super().__init__("star.png", position)
      
      self._speed = 500
      self._nFrames = 2
      self._framesPerSecond = 5.0
      
   
   def handleEvent(self, event):
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_DOWN:
            self._velocity[1] = self._speed
         elif event.key == pygame.K_UP:
            self._velocity[1] = -self._speed
         elif event.key == pygame.K_LEFT:
            self._velocity[0] = -self._speed
         elif event.key == pygame.K_RIGHT:
            self._velocity[0] = self._speed
      
      elif event.type == pygame.KEYUP:
         if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
            self._velocity[1] = 0
         elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            self._velocity[0] = 0
      