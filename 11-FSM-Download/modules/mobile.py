
from .animated import Animated
from .vector2D import Vector2

class Mobile(Animated):
   def __init__(self, imageName, position):
      super().__init__(imageName, position)
      self._velocity = Vector2(0,0)
      
   
   def update(self, seconds):
      
      super().update(seconds)
      
      self._velocity = Vector2(0,0)
      
      if self._state.getState() != "standing":
         currentFacing = self._state.getFacing()
         
         if self._state._movement["down"]:
            self._velocity[1] = self._vSpeed
         elif self._state._movement["up"]:
            self._velocity[1] = -self._vSpeed
         if self._state._movement["left"]:
            self._velocity[0] = -self._vSpeed
         elif self._state._movement["right"]:
            self._velocity[0] = self._vSpeed
            
         newPosition = self.getPosition() + self._velocity * seconds
         
         self.setPosition(newPosition)
      
      else:
         self._velocity = Vector2(0,0)
         
         

      
