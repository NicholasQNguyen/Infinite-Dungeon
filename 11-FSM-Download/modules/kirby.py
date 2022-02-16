from .mobile import Mobile
from .FSM import KirbyState
from .frameManager import FrameManager

import pygame

class Kirby(Mobile):
   def __init__(self, position):
      super().__init__("kirby.png", position)
      
      self._nFrames = 2
      self._vSpeed = 50 
      self._framesPerSecond = 2
      
      self._nFramesList = {
         "walking" : 4,
         "standing" : 2,
         "swimming" : 4
      }
      
      self._rowList = {
         "walking" : 1,
         "standing" : 0,
         "swimming" : 3
      }
      
      self._framesPerSecondList = {
         "walking" : 8,
         "standing" : 2,
         "swimming" : 8
      }
      
      self._state = KirbyState()
  
   def collide(self, collider):
      if collider == None:
         self._state.manageState("stopwater", self)
      else:
         self._state.manageState("startwater", self)
 
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
   
  
   def transitionState(self, state):
      self._nFrames = self._nFramesList[state]
      self._frame = 0
      self._row = self._rowList[state]
      self._framesPerSecond = self._framesPerSecondList[state]
      self._animationTimer = 0
      self.setImage(FrameManager.getInstance().getFrame(self._imageName, (self._row, self._frame)))
      
   
