
from .drawable import Drawable
from .vector2D import Vector2

class Mobile(Drawable):
   """A game object that can move."""
   def __init__(self, imageName, position, offset=None):
      super().__init__(imageName, position, offset = None)
      self._velocity = Vector2(0,0)
   
   def update(self, seconds):
      
      newPosition = self.getPosition() + self._velocity * seconds
      
      self.setPosition(newPosition)
      
      
