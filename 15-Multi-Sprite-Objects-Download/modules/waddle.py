from .mobile import Mobile
from .FSM import MobileState

import pygame

class WaddleDee(Mobile):
   def __init__(self, position):
      super().__init__("waddleDee.png", position)
      
      self._nFrames = 1
      self._vSpeed = 100
      self._aSpeed = 70
      self._framesPerSecond = 2
      
      self._nFramesList = {
         "moving" : 2,
         "standing" : 1
      }
      
      self._rowList = {
         "moving" : 1,
         "standing" : 0
      }
      
      self._framesPerSecondList = {
         "moving" : 8,
         "standing" : 1
      }
      
      self._state = MobileState()
      
      self._sight = 50
      self._forget = 100
      
   
   def think(self, kirby):
      distance = kirby.getPosition() - self._position
      
      if distance.magnitude() > self._forget:
         self._state.manageState("stopall", self)
      elif distance.magnitude() < self._sight:
         if kirby.getPosition().x < self._position.x:
            self._state.manageState("right", self)
         else:
            self._state.manageState("left", self)
         
         if kirby.getPosition().y < self._position.y:
            self._state.manageState("down", self)
         else:
            self._state.manageState("up", self)
   