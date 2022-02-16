
from .animated import Animated
from .vector2D import Vector2

class Mobile(Animated):
   def __init__(self, imageName, position):
      super().__init__(imageName, position)
      self._velocity = Vector2(0,0)      
      self._jumpTimer = 0
   
   def update(self, seconds, boundaries):
      
      super().update(seconds)
      
      if self._state.isMoving():        
         
         if self._state._movement["left"]:
            self._velocity.x = -self._vSpeed
         elif self._state._movement["right"]:
            self._velocity.x = self._vSpeed
      else:
         self._velocity.x = 0
      
            
      if self._state.getState() == "standing":
         self._velocity.y = 0         
      elif self._state.getState() == "jumping":
         self._velocity.y = -self._jSpeed
         self._jumpTimer -= seconds
         if self._jumpTimer < 0:
            self._state.manageState("fall", self)
            
      elif self._state.getState() == "falling":
         self._velocity.y += self._jSpeed * seconds
            
      
         
      newPosition = self.getPosition() + self._velocity * seconds
      
      if newPosition.x < 0 or newPosition.x > boundaries.x - self.getSize()[0]:
         self._velocity.x = -self._velocity.x
      if newPosition.y < 0 or newPosition.y > boundaries.y - self.getSize()[1]:
         self._velocity.y = -self._velocity.y
         
         
      newPosition = self.getPosition() + self._velocity * seconds
      
      self.setPosition(newPosition)
   
   def transitionState(self, state):
      
      if state == "jumping":
         self._jumpTimer = self._jumpTime
      
      super().transitionState(state)
   
   
      
         
         

      
 
      
         
         
         

      