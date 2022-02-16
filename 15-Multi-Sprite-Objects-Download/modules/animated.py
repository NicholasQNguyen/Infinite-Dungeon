import pygame
from pygame import image
import os
from .frameManager import FrameManager
from .drawable import Drawable
from .rotated import Rotatable

class AbstractAnimated(object):
   
   def __init__(self):      
      self._frame = 0
      self._row = 0
      self._animationTimer = 0
      self._framesPerSecond = 10.0
      self._nFrames = 2
      
      self._animate = True
      
   def update(self, seconds):
      if self._animate:
         self._animationTimer += seconds         
         if self._animationTimer > 1 / self._framesPerSecond:
            self._frame += 1
            self._frame %= self._nFrames
            self._animationTimer -= 1 / self._framesPerSecond
            self.setImage(FrameManager.getInstance().getFrame(self._imageName, (self._frame, self._row)))
  
   def transitionState(self, state):
      self._nFrames = self._nFramesList[state]
      self._frame = 0
      self._row = self._rowList[state]
      self._framesPerSecond = self._framesPerSecondList[state]
      self._animationTimer = 0
      self.setImage(FrameManager.getInstance().getFrame(self._imageName, (self._frame, self._row)))

class Animated(AbstractAnimated, Drawable):
   
   def __init__(self, imageName, position):
      super().__init__()
      Drawable.__init__(self, imageName, position, (0,0))
      
   
class AnimatedRotatable(AbstractAnimated, Rotatable):
   def __init__(self, imageName, position):
      super().__init__()
      Rotatable.__init__(self, imageName, position, (0,0))
      