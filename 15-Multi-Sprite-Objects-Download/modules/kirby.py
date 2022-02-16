from .mobile import Mobile, MobileRotatable
from .FSM import MobileState, MobileRotatableState
from .vector2D import Vector2
from .drawable import Drawable

import pygame


class Kirby(Mobile):
   def __init__(self, position):
      super().__init__("kirby.png", position)

      self._hat = Drawable("hat.png", position)
      self._hatOffset = Vector2(4, -6)      

      self._nFrames = 2
      self._vSpeed = 50
      self._aSpeed = 100
      self._framesPerSecond = 2
      
      self._nFramesList = {
         "moving" : 4,
         "swimming" : 4,
         "standing" : 2
      }
      
      self._rowList = {
         "moving" : 1,
         "swimming" : 3,
         "standing" : 0
      }
      
      self._framesPerSecondList = {
         "moving" : 8,
         "swimming" : 8,
         "standing" : 2
      }
      
      self._state = MobileState()      
   
   def handleEvent(self, event):
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_DOWN:
            self._state.manageState("down", self)
            
         elif event.key == pygame.K_UP:
            self._state.manageState("up", self)
            
         elif event.key == pygame.K_LEFT:
            self._state.manageState("left", self)
            
         elif event.key == pygame.K_RIGHT: self._state.manageState("right", self)
      elif event.type == pygame.KEYUP:
         if event.key == pygame.K_DOWN:
            self._state.manageState("stopdown", self)
            
         elif event.key == pygame.K_UP:
            self._state.manageState("stopup", self)
            
         elif event.key == pygame.K_LEFT:
            self._state.manageState("stopleft", self)
            
         elif event.key == pygame.K_RIGHT:
            self._state.manageState("stopright", self)

   def update(self, seconds, worldInfo):
      super().update(seconds, worldInfo)

      if self._state.getFacing() == "right":
         offset = self._hatOffset
      else:
         offset = Vector2(self.getWidth() - self._hatOffset.x - self._hat.getWidth(), self._hatOffset.y)

      self._hat.setPosition(self.getPosition() + offset)

   def draw(self, drawSurface):
      super().draw(drawSurface)
      self._hat.draw(drawSurface)


class KirbyRotatable(Mobile):
   def __init__(self, position):
      super().__init__("kirby.png", position)

      self._nFrames = 2
      self._vSpeed = 50
      self._aSpeed = 100
      self._framesPerSecond = 2
      
      self._nFramesList = {
         "moving" : 4,
         "swimming" : 4,
         "standing" : 2
      }
      
      self._rowList = {
         "moving" : 1,
         "swimming" : 3,
         "standing" : 0
      }
      
      self._framesPerSecondList = {
         "moving" : 8,
         "swimming" : 8,
         "standing" : 2
      }
      
      self._state = MobileRotatableState()      
   
   def handleEvent(self, event):
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_DOWN:
            self._state.manageState("down", self)
            
         elif event.key == pygame.K_UP:
            self._state.manageState("up", self)
            
         elif event.key == pygame.K_LEFT:
            self._state.manageState("left", self)
            
         elif event.key == pygame.K_RIGHT:
            self._state.manageState("right", self)
      
      elif event.type == pygame.KEYUP:
         if event.key == pygame.K_DOWN:
            self._state.manageState("stopdown", self)
            
         elif event.key == pygame.K_UP:
            self._state.manageState("stopup", self)
            
         elif event.key == pygame.K_LEFT:
            self._state.manageState("stopleft", self)
            
         elif event.key == pygame.K_RIGHT:
            self._state.manageState("stopright", self)
   def update(self, seconds, worldInfo):
      super().update(seconds, worldInfo)

   def draw(self, drawSurface):
      super().draw(drawSurface)


