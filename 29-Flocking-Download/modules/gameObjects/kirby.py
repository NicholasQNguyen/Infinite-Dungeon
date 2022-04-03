from .mobile import Mobile
from ..FSMs.topDownFSM import MobileState
from ..UI.screenInfo import adjustMousePos
from .vector2D import Vector2
import pygame

class Kirby(Mobile):
   def __init__(self, position):
      super().__init__("kirby.png", position)
      
      self._nFrames = 2
      self._vSpeed = 50
      self._aSpeed = 100
      self._framesPerSecond = 2
      
      self._nFramesList = {
         "walking" : 4,
         "swimming" : 4,
         "standing" : 2
      }
      
      self._rowList = {
         "walking" : 1,
         "swimming" : 3,
         "standing" : 0
      }
      
      self._framesPerSecondList = {
         "walking" : 8,
         "swimming" : 8,
         "standing" : 2
      }
      
      self._state = MobileState()
      self._debugDraw = False
      self._mousePos = Vector2(0,0)
   
   def handleEvent(self, event):
      # if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
      #     self._debugDraw = not self._debugDraw
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
            
      # elif event.type == pygame.MOUSEMOTION:
      #    self._mousePos = adjustMousePos(event.pos)
      #    angleToMouse = self._position + self._image.get_rect().center - self._mousePos
      #    print(angleToMouse.getAngle())
          
   def draw(self, surface):
      super().draw(surface)
      if self._debugDraw:
         pygame.draw.line(surface, (255,0,0), list(self._position + self._image.get_rect().center), list(self._mousePos), 1)
         pygame.draw.circle(surface, (255,0,0), list(self._mousePos), 3)

      
   