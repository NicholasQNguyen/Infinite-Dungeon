
from .animated import Animated
from .vector2D import Vector2

class Mobile(Animated):
   """A game object that can move."""
   def __init__(self, imageName, position):
      super().__init__(imageName, position)
      self._velocity = Vector2(0,0)
   
   def update(self, seconds):
      
      super().update(seconds)
      
      newPosition = self.getPosition() + self._velocity * seconds
      
      self.setPosition(newPosition)
      
      