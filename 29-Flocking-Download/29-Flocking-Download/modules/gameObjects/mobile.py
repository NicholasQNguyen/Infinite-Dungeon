
from .animated import Animated
from .vector2D import Vector2

class Mobile(Animated):
   def __init__(self, imageName, position):
      super().__init__(imageName, position)
      self._velocity = Vector2(0,0)
      
   
   def update(self, seconds, boundaries):
      
      super().update(seconds)
      
      if self._state.getState() != "standing":
         currentFacing = self._state.getFacing()
         
         if self._state._movement["down"]:
            self._velocity[1] += self._aSpeed * seconds
         elif self._state._movement["up"]:
            self._velocity[1] += -self._aSpeed * seconds
         if self._state._movement["left"]:
            self._velocity[0] += -self._aSpeed * seconds
         elif self._state._movement["right"]:
            self._velocity[0] += self._aSpeed * seconds
         
         if self._velocity.magnitude() > self._vSpeed:
            self._velocity.scale(self._vSpeed)
            
         newPosition = self.getPosition() + self._velocity * seconds
         
         if newPosition.x < 0 or newPosition.x > boundaries.x - self.getSize()[0]:
            self._velocity.x = -self._velocity.x
         if newPosition.y < 0 or newPosition.y > boundaries.y - self.getSize()[1]:
            self._velocity.y = -self._velocity.y
            
            
         newPosition = self.getPosition() + self._velocity * seconds
         
         self.setPosition(newPosition)
      
      else:
         self._velocity = Vector2(0,0)
         
         

      