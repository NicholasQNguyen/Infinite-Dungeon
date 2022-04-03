

from .animated import Animated
from .vector2D import Vector2
from ..managers.soundManager import SoundManager

class Explosion(Animated):
   
   
   def __init__(self, position, kirby):
      super().__init__("explosion.png", position - Vector2(16,16))
      
      self._noise = SoundManager.getInstance().playSound("explosion.wav", loop=0)
      SoundManager.getInstance().updateVolumePositional(self._noise, kirby.getPosition(), self.getPosition())
      
      self._frame = 0
      self._row = 0
      self._animationTimer = 0
      self._framesPerSecond = 20.0
      self._nFrames = 8
      self._lifetime = self._nFrames * (1/self._framesPerSecond)
      
      self._isDead = False
      
   
   def update(self, seconds, kirby):
      if self._lifetime <= (0.5 / self._framesPerSecond):
         self._isDead = True
      else:
         self._lifetime -= ticks
         super().update(ticks)
         SoundManager.getInstance().updateVolumePositional(self._noise, kirby.getPosition(), self.getPosition())
         
   
   def isDead(self):
      return self._isDead
      
      
   
   
      